from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import PostImageForm, PostCommentForm
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment
from django.contrib import messages
from django.http import HttpResponseRedirect
from account.models import Follow



"""
View to create a post
""" 
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

"""
View to display post details
""" 
@login_required()
def post_detail(request, id):
    user = request.user
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(visible=True)
    form = PostCommentForm()
    liked_by_user = Like.objects.filter(post=post, user=user).first()
    if liked_by_user is None:
        liked_by_user = False
    else:
        liked_by_user = True
    print(liked_by_user)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'liked_by_user': liked_by_user
    }
    return render(request, 'post/post_detail.html', context)

"""
View to return all current users posts
""" 
@login_required()
def current_user_posts(request):
    user = request.user
    user_posts = Post.objects.filter(user=user)
    post_count = user_posts.count()
    return render(request, 'post/user_posts.html', {'user_posts': user_posts, 'post_count': post_count})

"""
View to like a post
""" 
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

"""
View to delete a post of the currently logged in user
""" 
@login_required
def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.user == post.user:
        post.delete()
        return redirect('/', {'post': post})
    return redirect(request.META.get('HTTP_REFERER'))

"""
View to add a comment to a post
""" 
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


"""
View to delete a comment created but the currently logged in user
""" 
@login_required
def comment_delete(request, id):
    comment = Comment.objects.get(id=id)
    if request.user == comment.user:
        comment.delete()
    return redirect(request.META.get('HTTP_REFERER'), {'comment': comment})


# @login_required
# def followed_feed(request):
#     current_user = request.user
#     followed_accounts = Follow.objects.filter(user=user)
#     user_following_feed = []
#     feed_posts = []
#     for account in followed_accounts:
#         user_following_feed.append(account)
#     for usernames in user_following_feed:
#         feed_lists = Post.objects.filter(user=usernames)
#         feed_posts.append(feed_lists)
#     context = {
#         'feed_posts': feed_posts
#     }
#     print(user_following_feed)
#     return render(request, 'post/feed.html', context)

"""
View to return all posts by latest
""" 
@login_required
def latest_posts(request):
    all_posts = Post.objects.all()
    post_count = all_posts.count()
    return render(request, 'post/feed.html', {'all_posts': all_posts, 'post_count': post_count})


        


        


