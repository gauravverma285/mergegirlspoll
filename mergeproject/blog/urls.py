from django.urls import path
from . import views

from .views import SignUpView #1
# app_name = "blog"
from .views import profile

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='users-profile'),
    path('category/', views.category_list, name='category_list'),

    path("signup/", SignUpView.as_view(), name="signup"), #1

    # path("", views.homepage, name="homepage"),
    # path("signup", views.signup, name="signup")
]

