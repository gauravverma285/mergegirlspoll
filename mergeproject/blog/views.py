from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .form import PostForm

from django.shortcuts import redirect


from django.shortcuts import get_object_or_404

# Create your views here.
from . import forms
from django.contrib.auth import login, authenticate  

from django.urls import reverse_lazy  #1
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "blog/signup.html" #1


def post_list(request):
    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': 'posts'})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def login(request, pk):
    login = get_object_or_404(login, pk=pk)
    return render(request, 'blog/login.html', {'login': login})

from django.contrib.auth import login, authenticate  # add to imports

def login(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'blog/login.html', context={'form': form, 'message': message})

def signup(request, pk):
    login = get_object_or_404(signup, pk=pk)
    return render(request, 'blog/signup.html', {'signup': signup})

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('signup', pk=post.pk)
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

