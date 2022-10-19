from django.contrib import admin
from .models import Category, Post, CustomUser
from .models import Profile

# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ["email", "username",]

admin.site.register(CustomUser)

admin.site.register(Post)

admin.site.register(Profile)
admin.site.register(Category)