import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")   # ← use the service role here

if not URL or not KEY:
    raise RuntimeError("Supabase URL or SERVICE_ROLE key missing")

supabase = create_client(URL, KEY)
