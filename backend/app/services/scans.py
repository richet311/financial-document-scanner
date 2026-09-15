from app.core.logging import logger
from app.services.supabase_client import get_user_scoped_client


class ScanPersistenceError(Exception):
    """Raised when a scan result could not be saved to Supabase."""


def save_scan(
    *,
    access_token: str,
    user_id: str,
    filename: str,
    document_type: str | None,
    confidence: float | None,
    fields: dict[str, float],
    insights: list[str],
) -> None:
    client = get_user_scoped_client(access_token)
    try:
        client.table("scans").insert(
            {
                "user_id": user_id,
                "filename": filename,
                "document_type": document_type,
                "confidence": confidence,
                "fields": fields,
                "insights": insights,
            }
        ).execute()
    except Exception as exc:
        logger.error("Failed to persist scan for user %s: %s", user_id, exc)
        raise ScanPersistenceError(str(exc)) from exc
