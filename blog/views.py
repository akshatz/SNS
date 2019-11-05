# from django.http import request
from django_project.settings import AUTH_USER_MODEL
from .models import Posts
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

user = get_user_model()


def home_view(request):
    if request.user.is_authenticated:
        context = {
            'posts': Posts.objects.filter(author=request.user)
        }
        # print(context)
        return render(request, 'blog/home.html', context)


class PostDetailView(DetailView):
    if user.is_authenticated:
        model = Posts
    else:
        redirect('blog/')

    def get_queryset(self):
        return Posts.objects.filter(author=self.request.user)


class PostCreateView(LoginRequiredMixin, CreateView):

    """Post form has fields
        title
        content
        image
    """
    fields = ['title', 'content', 'image']
    model = Posts

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Post update form  has fields
        title
        content
        image
    """
    model = Posts
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class UserPostListView(ListView):
    model = Posts
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(AUTH_USER_MODEL, username=self.kwargs.get('pk'))
        return Posts.objects.filter(author=user).order_by('-date_posted')

