from django.urls import path
from . import views

from .views import SignUpView #1

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('login/', views.login, name='login'),
    path('signup/', views.login, name='signup'),

    path("signup/", SignUpView.as_view(), name="signup"), #1
]

