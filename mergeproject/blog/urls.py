from django.urls import path
from . import views

from .views import signup #1
from .views import profile, login, logout

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('show/', views.show, name='show'),
    path('profile/', views.profile, name='profile'),
    path('category/<str:slug>/', views.category_list, name='category_list'),
    path('tag/', views.tag_list, name='tag_list'),
]

