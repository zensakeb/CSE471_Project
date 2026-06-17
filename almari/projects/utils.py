# projects/utils.py
# projects/utils.py

from urllib import request
import uuid
from users.supabase_client import supabase
from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from users.supabase_client import supabase  # adjust if needed


def upload_project_image(image_file):
    """
    Uploads a Django InMemoryUploadedFile to Supabase Storage and returns its public URL.
    """
    # 1) Generate a unique filename and path
    ext      = image_file.name.rsplit('.', 1)[-1].lower()
    filename = f"{uuid.uuid4()}.{ext}"
    bucket   = "project-images"
    path     = filename          # no nested folders
    
    # 2) Read the bytes and upload
    file_bytes = image_file.read()
    res = supabase.storage.from_(bucket).upload(path, file_bytes, {
        "content-type": image_file.content_type,
        "x-upsert": "true"
    })
    # if your version returns an error attribute
    if getattr(res, "error", None):
        print("Supabase upload error:", res.error)
        return None

    # 3) Get the public URL
    public_url = supabase.storage.from_(bucket).get_public_url(path)
    # this client sometimes returns a dict, sometimes a str:
    if isinstance(public_url, str):
        return public_url
    # else it might be { "publicURL": "..."}
    return public_url.get("publicURL") or public_url.get("public_url")

# projects/utils.py

