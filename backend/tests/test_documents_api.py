import app.api.routes.documents as documents_module
from app.services.classifier import ClassifierNotTrainedError


def test_upload_rejects_invalid_type(client):
    response = client.post(
        "/api/documents/upload",
        files={"file": ("bad.txt", b"just plain text", "text/plain")},
    )
    assert response.status_code == 400


def test_upload_success(client, monkeypatch):
    monkeypatch.setattr(
        documents_module,
        "extract_text",
        lambda contents, content_type: "Gross Income: $5000.00\nNet Pay: $3800.00",
    )
    monkeypatch.setattr(
        documents_module,
        "classify_document",
        lambda text: {"document_type": "pay_stub", "confidence": 0.99},
    )

    response = client.post(
        "/api/documents/upload",
        files={"file": ("stub.pdf", b"%PDF-1.4 fake content", "application/pdf")},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["document_type"] == "pay_stub"
    assert body["fields"]["gross_income"] == 5000.0
    assert any("withheld" in insight for insight in body["insights"])
    assert body["saved"] is False


def test_upload_saves_scan_when_signed_in(authed_client, monkeypatch):
    monkeypatch.setattr(
        documents_module, "extract_text", lambda contents, content_type: "Balance: $100.00"
    )
    monkeypatch.setattr(
        documents_module,
        "classify_document",
        lambda text: {"document_type": "bank_statement", "confidence": 0.9},
    )

    saved_calls = []
    monkeypatch.setattr(
        documents_module,
        "save_scan",
        lambda **kwargs: saved_calls.append(kwargs),
    )

    response = authed_client.post(
        "/api/documents/upload",
        headers={"Authorization": "Bearer fake-token"},
        files={"file": ("statement.pdf", b"%PDF-1.4 fake content", "application/pdf")},
    )
    assert response.status_code == 200
    assert response.json()["saved"] is True
    assert len(saved_calls) == 1
    assert saved_calls[0]["user_id"] == "test-user-id"
    assert saved_calls[0]["document_type"] == "bank_statement"


def test_upload_still_works_if_save_fails(authed_client, monkeypatch):
    from app.services.scans import ScanPersistenceError

    monkeypatch.setattr(
        documents_module, "extract_text", lambda contents, content_type: "some text"
    )
    monkeypatch.setattr(
        documents_module,
        "classify_document",
        lambda text: {"document_type": "budget_sheet", "confidence": 0.8},
    )

    def _raise_persistence_error(**kwargs):
        raise ScanPersistenceError("Supabase unreachable")

    monkeypatch.setattr(documents_module, "save_scan", _raise_persistence_error)

    response = authed_client.post(
        "/api/documents/upload",
        headers={"Authorization": "Bearer fake-token"},
        files={"file": ("sheet.pdf", b"%PDF-1.4 fake content", "application/pdf")},
    )
    assert response.status_code == 200
    assert response.json()["saved"] is False


def test_upload_handles_untrained_classifier(client, monkeypatch):
    def _raise_not_trained(text):
        raise ClassifierNotTrainedError("not trained")

    monkeypatch.setattr(
        documents_module, "extract_text", lambda contents, content_type: "some text"
    )
    monkeypatch.setattr(documents_module, "classify_document", _raise_not_trained)

    response = client.post(
        "/api/documents/upload",
        files={"file": ("doc.pdf", b"%PDF-1.4 fake content", "application/pdf")},
    )
    assert response.status_code == 200
    assert response.json()["document_type"] is None
