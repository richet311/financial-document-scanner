from functools import lru_cache

from supabase import Client, create_client

from app.core.config import settings


class SupabaseNotConfiguredError(Exception):
    """Raised when SUPABASE_URL / SUPABASE_ANON_KEY are not set."""


@lru_cache
def get_anon_client() -> Client:
    if not settings.supabase_url or not settings.supabase_anon_key:
        raise SupabaseNotConfiguredError("Supabase is not configured on this server.")
    return create_client(settings.supabase_url, settings.supabase_anon_key)


def get_user_scoped_client(access_token: str) -> Client:
    """A fresh client authenticated as the given user, so Postgres row-level
    security policies see the real auth.uid(). Deliberately not the cached
    singleton: postgrest.auth() mutates client state, which would leak one
    request's token into another's if requests shared a client instance."""
    if not settings.supabase_url or not settings.supabase_anon_key:
        raise SupabaseNotConfiguredError("Supabase is not configured on this server.")
    client = create_client(settings.supabase_url, settings.supabase_anon_key)
    client.postgrest.auth(access_token)
    return client
