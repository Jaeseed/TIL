from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm,CommentForm
from users.models import User
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
@login_required
def main(request):
    user = request.user
    posts = Post.objects.all()
    comment_form = CommentForm()
    comments = user.post_author.all()
    context = {
        'posts': posts,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'posts/main.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        user = request.user
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('posts:main')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)


def personal(request,pk):
    user = get_object_or_404(User, pk=pk)
    posts = user.post_author.all()
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'posts/personal.html', context)


def comment_create(request, pk):
    pass