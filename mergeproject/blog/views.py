from django.shortcuts import render
from django.utils import timezone
# from requests import post

from .models import Post, CustomUser
from .forms import PostForm, CustomUserCreationForm, LoginForm

from django.shortcuts import redirect


from django.shortcuts import get_object_or_404

# from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth import login, authenticate

# Create your views here.
from . import forms
# from django.contrib.auth import login, authenticate  
# from django.contrib.auth import login, authenticate  # add to imports

from django.urls import reverse_lazy  #1
from django.views.generic.edit import CreateView

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from requests import request



# from django.contrib.auth.decorators import login_required

# from django.contrib import messages

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

# def login_view(request, pk):
#     login = get_object_or_404(login, pk=pk)
#     return render(request, 'blog/login.html', {'login': login})

def login_view(request):
    form = forms.LoginForm()
    if request.method =='POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form,'00000')
            
            # print(username, password,'111111111111111')
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                print(user, "555555555")
                return redirect('post_list')
            else:
                form = forms.LoginForm()
    return render (request, "blog/login.html", {"form" : form})
            


# def signup(request, pk):
#     signup = get_object_or_404(signup, pk=pk)
#     return render(request, 'blog/signup.html', {'signup': signup})

def signup(request):
    form = forms.CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username='username', password='raw_password')
            login(request, user)
            return redirect('post_list')
        else:
            form = forms.CustomUserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request, pk):
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


# def sign_up(request):
#     fm = UserCreationForm()
#     return render(request, 'blog/signup.html', {'form': fm})

