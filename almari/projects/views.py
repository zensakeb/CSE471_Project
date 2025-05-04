# projects/views.py

from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from .utils import upload_project_image
from .utils import upload_project_image
from users.supabase_client import supabase  # adjust if needed
from datetime import datetime

now = datetime.utcnow().isoformat()

# projects/views.py


# projects/views.py
@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES.get("image_file")
            image_url = None

            if image_file:
                image_url = upload_project_image(image_file)
                if not image_url:
                    form.add_error("image_file", "Image upload failed, please try again.")
                    return render(request, "projects/create_project.html", {"form": form})

            # Build data for Supabase
            data = {
                "title": form.cleaned_data["title"],
                "description": form.cleaned_data["description"],
                "category": form.cleaned_data["category"],
                "quantity": form.cleaned_data["quantity"],
                "tags": form.cleaned_data["tags"],
                "image_url": image_url,
                "user_id": request.user.id,
                "created_at": now,
                "updated_at": now,
            }

            # Insert into Supabase
            try:
                res = supabase.table("projects_project").insert(data).execute()
            except Exception as e:
                messages.error(request, f"Project creation failed: {e}")
                return redirect("create_project")
            
            return redirect("projects:my_projects")

    else:
        form = ProjectForm()

    return render(request, "projects/create_project.html", {"form": form})



@login_required
def my_projects(request):
    user_id = request.user.id
    res = supabase.table("projects_project").select("*").eq("user_id", user_id).execute()

    projects = res.data if res.data else []

    return render(request, "projects/project_list.html", {"projects": projects})


@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)

            image = form.cleaned_data.get("image_file")
            if image:
                url = upload_project_image(image)
                if url:
                    project.image_url = url
                else:
                    form.add_error("image_file", "Upload failed. Please try again.")

            project.save()
            return redirect("projects:my_projects")
    else:
        form = ProjectForm(instance=project)

    return render(request, "projects/edit_project.html", {"form": form})


@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)

    if request.method == "POST":
        project.delete()
        return redirect("projects:my_projects")

    return redirect("projects:my_projects")



