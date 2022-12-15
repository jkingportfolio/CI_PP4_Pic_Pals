from django.shortcuts import render
from .forms import PostImageForm
from django.contrib.auth.decorators import login_required

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
    return render(request, 'new_post.html', context)