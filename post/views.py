from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import PostImageForm
from django.contrib.auth.decorators import login_required
from .models import Post, Follow, Feed


# Create your views here.
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostImageForm(request.POST, request.FILES)
        if form.is_valid():
            # clear_form = form.cleaned_data
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return render(request, 'post/create_post.html', {'form':form})
    else:
        form = PostImageForm()
    return render(request, 'post/create_post.html', {'form':form})
    


@login_required()
def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post/post_detail.html', {'section': post})


@login_required()
def current_user_posts(request):
    user = request.user
    user_posts = Feed.objects.filter(user=user)
    post_list = []
    for post in user_posts:
        post_list.append(post.id)
    post_objects = Post.objects.filter(id__in=post_list).all().order_by('-created_date')
    context = {
        'post_objects': post_objects
    }
    return render(request, 'post/user_posts.html', context)