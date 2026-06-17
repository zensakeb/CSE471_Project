# users/pipeline.py
from .supabase_client import supabase
from django.contrib.auth.hashers import make_password

def sync_user_to_supabase(strategy, details, user=None, *args, **kwargs):
    if user is None:
        return

    payload = {
          "id": str(user.id),
        "username": user.username or "",
        "email": user.email or "",
        "first_name": user.first_name or "",  # ⬅️ added
        "last_name": user.last_name or "",    # ⬅️ optional but recommended
        "date_joined": user.date_joined.isoformat() if user.date_joined else None,
        "is_superuser": user.is_superuser,
        "is_staff": user.is_staff,
        "is_active": user.is_active,
        "password": make_password(None),
    }

    # Debug
    print("UPSERT PAYLOAD:", payload)

    # Use the exact table name
    response = supabase.table("users_customuser").upsert(payload).execute()
    print("SUPABASE RESPONSE:", response)
