from django.contrib import admin
from .models import Post, CustomUser

# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ["email", "username",]

admin.site.register(CustomUser)

admin.site.register(Post)