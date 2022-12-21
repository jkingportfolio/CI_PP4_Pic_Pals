from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import PostImageForm
from django.contrib.auth.decorators import login_required
from .models import Post, Follow, Feed, Like
from django.contrib import messages
from django.http import HttpResponseRedirect


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
            messages.success(request, 'Post added successfully')
            return redirect(new_post.get_absolute_url())
    else:
        form = PostImageForm()
    return render(request, 'post/create_post.html', {'form':form})    


@login_required()
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post/post_detail.html', {'post': post})


@login_required()
def current_user_posts(request):
    user = request.user
    user_posts = Post.objects.filter(user=user)
    return render(request, 'post/user_posts.html', {'user_posts': user_posts})

@login_required
def post_like(request):
    username = request.user.username
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)
    like_status = Like.objects.filter(post_id=post_id, username=username).first()

    if like_status == None:
        like = Like.objects.create(post_id=post_id, username=username)
        like.savee()
        post.likes = post.likes + 1
        post.save()
    else:
        like_status.delete()
        post.likes = post.likes - 1
        post.save()
    return redirect(ost.get_absolute_url())
