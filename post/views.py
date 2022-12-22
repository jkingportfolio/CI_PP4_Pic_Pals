from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import PostImageForm, PostCommentForm
from django.contrib.auth.decorators import login_required
from .models import Post, Follow, Feed, Like, Comment
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
    return render(request, 'post/create_post.html', {'form': form})


@login_required()
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(visible=True)
    form = PostCommentForm()
    return render(request, 'post/post_detail.html', {'post': post, 'comments': comments, 'form': form})


@login_required()
def current_user_posts(request):
    user = request.user
    user_posts = Post.objects.filter(user=user)
    return render(request, 'post/user_posts.html', {'user_posts': user_posts})


@login_required
def post_like(request, post):
    user = request.user
    post = Post.objects.get(id=post)
    like_status = Like.objects.filter(post=post, user=user).first()

    if like_status == None:
        like = Like.objects.create(post=post, user=user)
        like.save()
        post.likes = post.likes + 1
    else:
        like_status.delete()
        post.likes = post.likes - 1
    post.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.user == post.user:
        Post.objects.get(id=id).delete()
    return redirect('/')


@login_required
def post_comment(request, id):
    user = request.user
    post = get_object_or_404(Post, id=id)
    comment = None
    form = PostCommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = user
        comment.post = post
        comment.save()
    return redirect(request.META.get('HTTP_REFERER'), {'post': post,
                                                       'form': form,
                                                       'comment': comment})


@login_required
def follow_user(request, user_name):
    user_to_follow = User.objects.get(name=user_name)
    current_user = request.user
    follow_status = Followers.objects.get(user=get_user.id)
    is_followed = False
    if user_to_follow.name != current_user:
        if follow_status.another_user.filter(name=user_to_follow).exists():
            add_follow_obj = Followers.objects.get(user=current_user)
            add_follow_obj.another_user.remove(user_to_follow)
            is_followed = False
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            add_follow_obj = Followers.objects.get(user=get_user)
            add_follow_obj.another_user.add(user_to_follow)
            is_followed = True
            return redirect(request.META.get('HTTP_REFERER'))

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))
