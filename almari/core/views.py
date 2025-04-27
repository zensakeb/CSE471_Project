from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

def social_wall(request):
    from social.models import SocialWallPost
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        # Create new post
        post = SocialWallPost.objects.create(
            user=request.user,
            image=image,
            caption=f"{title}\n\n{description}"
        )
    
    # Get all posts for display
    posts = SocialWallPost.objects.all().order_by('-created_at')
    return render(request, 'core/social_wall.html', {'posts': posts})