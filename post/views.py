"""
A module for views of the post app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
import datetime
# Internal
from .models import Post, Like, Comment
from .forms import PostImageForm, PostCommentForm, EditPost
from account.models import Follow
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@login_required
def create_post(request):
    """
    A function based view for the create post page in which
    a user can upload an image alongside a caption
    """
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
def edit_post(request, id):
    """
    A function based view to display a form to allow the owner
    of a post to edit the caption of the post
    """
    post = Post.objects.get(id=id)
    if not request.user == post.user:
        messages.error(request, 'Sorry, you do not have permission to do that.')
        return redirect(reverse('dashboard'))
    if request.method == 'POST':
        post_form = EditPost(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            post.caption_edited = True
            post.caption_edited_time = datetime.datetime.now()
            post.save()
            messages.success(request, 'Post caption updated successfully.')
        else:
            messages.error(request, 'Error updating post caption.')
    else:
        post_form = EditPost(instance=post)
    context = {
        'form': post_form,
        'post': post,
    }
    return render(request, 'post/edit_post.html', context)


@login_required()
def post_detail(request, id):
    """
    A function based view to display a post and allow users
    the chance to add a comment
    """
    user = request.user
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()
    form = PostCommentForm()
    liked_by_user = Like.objects.filter(post=post, user=user).first()
    if liked_by_user is None:
        liked_by_user = False
    else:
        liked_by_user = True
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'liked_by_user': liked_by_user
    }
    return render(request, 'post/post_detail.html', context)


@login_required()
def current_user_posts(request):
    """
    A function based view to view a list of all the current
    users posts
    """
    user = request.user
    user_posts = Post.objects.filter(user=user)
    post_count = user_posts.count()
    return render(request, 'post/user_posts.html', {'user_posts': user_posts, 'post_count': post_count})


@login_required
def post_like(request, post):
    """
    A function based view to allow the ability to 
    like an unlike a post
    """
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
    """
    A function based view to allow a user to delete their
    own posts
    """
    post = Post.objects.get(id=id)
    if request.user == post.user:
        post.delete()
        messages.success(request, 'Post deleted successfully.')
        return redirect('/', {'post': post})
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def post_comment(request, id):
    """
    A function based view to allow a user to add a comment
    to a post
    """
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
def comment_delete(request, id):
    """
    A function based view to allow a user to delete their comment
    and any comment if the user owns the post
    """
    comment = Comment.objects.get(id=id)
    post = comment.post
    if request.user == comment.user or request.user == post.user:
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
    return redirect(request.META.get('HTTP_REFERER'), {'comment': comment})


@login_required
def followed_feed(request):
    """
    A function based view to display the current users feed
    which consists of all posts of the accounts followed
    """
    user_following_feed = []
    followed_user_posts = []
    current_user = request.user
    followed_accounts_current_user = Follow.objects.filter(user=current_user)
    for account in followed_accounts_current_user:
        user_following_feed.append(account.followed_account.username)
    followed_user_posts = Post.objects.filter(
        user__username__in=user_following_feed)
    context = {
        'followed_user_posts': followed_user_posts,
    }
    return render(request, 'post/feed.html', context)
    
