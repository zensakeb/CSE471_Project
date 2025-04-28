from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomProduct, Product
from .forms import CustomProductForm
from django.contrib.auth import login
from .forms import SignUpForm

@login_required
def delete_project(request, pk):
    project = get_object_or_404(CustomProduct, pk=pk, user=request.user)
    project.delete()
    return redirect('user_projects')

@login_required
def edit_project(request, pk):
    project = get_object_or_404(CustomProduct, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CustomProductForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('user_projects')
    else:
        form = CustomProductForm(instance=project)
    return render(request, 'upload.html', {'form': form})
@login_required
def upload_custom_product(request):
    if request.method == 'POST':
        form = CustomProductForm(request.POST, request.FILES)
        if form.is_valid():
            custom = form.save(commit=False)
            custom.user = request.user
            custom.save()
            return redirect('user_projects')
    else:
        form = CustomProductForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def user_projects(request):
    projects = CustomProduct.objects.filter(user=request.user)
    return render(request, 'my_projects.html', {'projects': projects})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user
            return redirect('upload_custom_product')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def upload_start(request):
    return render(request, 'upload_start.html')
