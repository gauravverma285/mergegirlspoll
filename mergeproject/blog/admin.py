from django.contrib import admin
from .models import Category, Post, CustomUser, Tag, Comment, ReplyComment
from .models import Profile
from import_export.admin import ExportActionMixin

# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ["email", "username",]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

# @admin.register(Post)
class PostAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('author', 'title', 'published_date', 'created_date', 'category')
    list_filter = ['published_date', 'created_date', 'author', 'title' ]
    search_fields = ['title','author']

class CategoryAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name']

class TagAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name']

class ProfileAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ['user']
    search_fields = ['user']
    
    # fieldsets = [
    #     (None,               {'fields': ['title']}),
    #     ('Date information', {'fields': ['published_date'], 'classes': ['collapse']}),
    # ]

admin.site.register(CustomUser)

admin.site.register(Post, PostAdmin)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
# admin.site.register(ReplyComment)