from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.supabase_client import supabase
@login_required
def about(request):
    return render(request, 'core/about.html')

@login_required
def contact(request):
    return render(request, 'core/contact.html')

from django.shortcuts import render

def core_home(request):
    return render(request, "core/frontpage.html")  # Create this template

# core/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.supabase_client import supabase


@login_required
def frontpage(request):
    category = request.GET.get("category")
    tag      = request.GET.get("tag")
    
    query = supabase.table("projects_project").select("*").order("created_at", desc=True)
    if category:
        query = query.eq("category", category)
    if tag:
        query = query.ilike("tags", f"%{tag}%")

    try:
        res = query.execute()
        projects = res.data
    except Exception as e:
        print(f"Error retrieving projects: {e}")
        projects = []

    return render(request, "core/frontpage.html", {
        "projects":   projects,
        "username":   request.user.username,
        "user_id":    request.user.id,
    })
