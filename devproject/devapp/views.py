# from github repository shaurya-blip/code
# link -> https://www.github.com/shaurya-blip/code
# Copyrights registered shaurya-blip2020

from django.views.generic import DetailView,ListView,CreateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Comment
from .forms import CommentForm
from django.views import generic
# Create your views here.

class IndexClass(ListView):
    model = Post
    template_name = 'devapp/index.html'

class IndexDetail(DetailView):
    model = Post
    template_name = 'devapp/post_detail.html'

# class CommentCreate(CreateView):
#     model = Comment
#     fields = ('post','author','phone','text','created_date')
#     template_name = 'devapp/new_comment.html'

class CommentList(ListView):
    model = Comment
    template_name = 'devapp/post_detail.html'


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'devapp/new_comment.html', {'form': form})
