import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture
def client(monkeypatch):
    # Avoid loading real OCR/ML models during tests: fast, hermetic, no
    # network access or trained-model file required.
    monkeypatch.setattr("app.main.get_reader", lambda: None)
    monkeypatch.setattr("app.main.get_model", lambda: None)

    from app.main import app

    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def authed_client(client):
    """A client where get_optional_user resolves to a fake signed-in user,
    without needing a real Supabase project reachable during tests."""
    from app.core.deps import CurrentUser, get_optional_user
    from app.main import app

    fake_user = CurrentUser(id="test-user-id", email="demo@example.com", access_token="fake-token")
    app.dependency_overrides[get_optional_user] = lambda: fake_user
    yield client
    app.dependency_overrides.pop(get_optional_user, None)
