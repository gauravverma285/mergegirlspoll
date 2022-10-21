from unicodedata import category
from django import forms

from .models import Post, Comment, ReplyComment

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django.contrib.auth.models import User
from .models import Profile


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'category', 'tags', 'image', 'thumbnail_image',)


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ("username", "email",)

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ("username", "password",)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body',)


class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model = ReplyComment
        fields = ('replier_name', 'reply_content')