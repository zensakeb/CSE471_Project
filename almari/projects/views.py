# projects/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from .utils import upload_project_image, get_all_projects

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user

            image = request.FILES.get("image")
            if image:
                url = upload_project_image(image)
                if url:
                    project.image_url = url
                else:
                    form.add_error("image", "Upload failed. Please try again.")

            project.save()
            return redirect("projects:my_projects")

    else:
        form = ProjectForm()

    return render(request, "projects/create_project.html", {"form": form})


@login_required
def my_projects(request):
    qs = Project.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "projects/project_list.html", {"projects": qs})


@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)

            image = request.FILES.get("image")
            if image:
                url = upload_project_image(image)
                if url:
                    project.image_url = url
                else:
                    form.add_error("image", "Upload failed. Please try again.")

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

# projects/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import get_all_projects

@login_required
def frontpage(request):
    # pull all projects from Supabase
    projects = get_all_projects()
    print("Projects from Supabase:", projects)
    return render(request, "core/frontpage.html", {
        "projects": projects,
        "username": request.user.username,
        "user_id": request.user.id,
    })

