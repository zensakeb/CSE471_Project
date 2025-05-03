# utils.py
import uuid
from users.supabase_client import supabase  # Adjust path if needed

def upload_project_image(image):
    ext = image.name.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    path = f"project-images/{filename}"

    # Upload to Supabase Storage
    res = supabase.storage.from_('project-images').upload(path, image.read(), {
        "content-type": image.content_type,
    })

    if hasattr(res, "error") and res.error:
        print("Upload error:", res.error)
        return None

    # Get public URL
    public_url = supabase.storage.from_('project-images').get_public_url(path)
    return public_url


def get_all_projects():
    """
    Fetch all rows from the 'projects' table in Supabase.
    Returns a list of dicts, each representing one project.
    """
    # Adjust the table name if yours is different
    response = supabase.table("projects_project").select("*").execute()
    if response.error:
        # you might log this
        return []
    return response.data  # list of {"id":..., "title":..., "image_url":..., etc.}
