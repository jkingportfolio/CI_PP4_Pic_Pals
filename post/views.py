from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostImageForm
from django.contrib.auth.decorators import login_required
from .models import Post


# Create your views here.
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostImageForm(data=request.POST)
        if form.is_valid():
            clear_form = form.cleaned_data
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
    else:
        form = PostImageForm()
    context = {'form': form}
    return render(request, 'create_post.html', context)


@login_required()
def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    return render(request, 'post/post_detail.html', {'section': post})


@login_required()
def current_user_posts(request):
    user_posts = Post.objects.filter(user=self.request.user)

    return render(request, 'post/user_posts.html', {'section': 'post'})