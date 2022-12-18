from django.forms import ImageField
from django.shortcuts import render
from django.utils import timezone
from .models import Comment, Post, CustomUser, Category, Tag, ReplyComment, Profile
from .forms import PostForm, ReplyCommentForm, CustomUserCreationForm, LoginForm, UpdateUserForm, UpdateProfileForm, CommentForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate, logout
from . import forms
# from django.contrib.auth import login, authenticate  
# from django.contrib.auth import login, authenticate  # add to imports
from django.urls import reverse_lazy  #1
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from requests import request
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator



# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "blog/signup.html" 


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    post = Post.objects.all()

    paginator = Paginator(post, 6) #show 6 post per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        title = request.POST.get("search_filter")
        if title != None:
            page_obj = Post.objects.filter(title__icontains=title)

#     send_mail(
#     'Testing Purpose',
#     'hhhhhhhhhhhh',
#     'gaurav998290@gmail.com',
#     ['gv894708@gmail.com'],
#     fail_silently=False,
# )
    return render(request, 'blog/post_list.html', {'posts': posts, 'page_obj': page_obj, 'page_obj': page_obj})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = comment_form.save(commit=False)
                    replay_comment.parent = parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/post_detail.html',
                  {'post': post,
                   'comments': comments,
                   'comment_form': comment_form})


# def login_view(request, pk):
#     login = get_object_or_404(login, pk=pk)
#     return render(request, 'blog/login.html', {'login': login})

@login_required
def show(request, username):
    user = get_object_or_404(CustomUser, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'blog/show.html', {'profile': profile, 'user': user})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        #profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid(): #and profile_form.is_valid():
            user_form.save()
            #profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        #profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'blog/profile.html', {'user_form': user_form})
   # , 'profile_form': profile_form

# @login_required
# def profile_edit(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect('profile_edit')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)

#     return render(request, 'blog/profile.html', {'user_form': user_form, 'profile_form': profile_form})
    
   

#for chnage password
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'blog/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('profile')

def logout_user(request):
    logout(request)
    return redirect('login')

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
            # subject = 'welcome to my Blogs.'
            # message = f'Hi {user.username}, thank you for registering in Blog app.'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = ['gv894708@gmail.com']
            # print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
            # send_mail( subject, message, email_from, recipient_list )

            return redirect('post_list')
        else:
            form = forms.CustomUserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

# def post_new(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            subject = 'welcome to my Blogs.'
            message = f'Hi { post.author }, thank you for Creating New Post.'
            # messagee = f'{ post.title }, this is your post title.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['gv894708@gmail.com']
            print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
            send_mail( subject, message, email_from, recipient_list )

            return redirect('post_detail', post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


# def sign_up(request):
#     fm = UserCreationForm()
#     return render(request, 'blog/signup.html', {'form': fm})

def category_list(request, slug):
    post= get_object_or_404(Post, slug=slug)
    posts = Post.objects.filter(category=post.category)
    
    return render(request, "blog/category_list.html", {'posts': posts})

def tag_list(request):
    tag = Tag.objects.filter()
    post = Post.objects.filter(tags = tag)
    # tags = Tag.objects.all()

    return render (request, 'blog/tag_list.html', {'post':post})
