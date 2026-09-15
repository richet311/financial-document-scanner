from dataclasses import dataclass

from fastapi import Header, HTTPException, status

from app.services.supabase_client import SupabaseNotConfiguredError, get_anon_client


@dataclass
class CurrentUser:
    id: str
    email: str | None
    access_token: str


def _resolve_user(token: str) -> CurrentUser:
    try:
        client = get_anon_client()
        response = client.auth.get_user(token)
    except SupabaseNotConfiguredError:
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token"
        ) from exc

    if not response or not response.user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token"
        )

    return CurrentUser(id=response.user.id, email=response.user.email, access_token=token)


async def get_current_user(
    authorization: str | None = Header(default=None),
) -> CurrentUser:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token"
        )
    token = authorization.removeprefix("Bearer ")
    try:
        return _resolve_user(token)
    except SupabaseNotConfiguredError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)
        ) from exc


async def get_optional_user(
    authorization: str | None = Header(default=None),
) -> CurrentUser | None:
    """Like get_current_user, but returns None instead of raising when
    there's no bearer token or Supabase isn't configured, so uploads keep
    working anonymously without persisting anything."""
    if not authorization or not authorization.startswith("Bearer "):
        return None
    token = authorization.removeprefix("Bearer ")
    try:
        return _resolve_user(token)
    except (SupabaseNotConfiguredError, HTTPException):
        return None
