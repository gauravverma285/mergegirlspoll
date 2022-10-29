from django.urls import path
from . import views

from .views import signup #1
# app_name = "blog"
from .views import profile, login, logout

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('show/', views.profile, name='show'),
    path('profile/', views.profile, name='profile'),
    path('category/', views.category_list, name='category_list'),
    path('tag/', views.tag_list, name='tag_list'),
    # path('replycomment/', views.replyComment, name='replycomment'),
    # path('image/', views.featured_image, name='featured_image'),


    # path("signup/", SignUpView.as_view(), name="signup"), #1

    # path("", views.homepage, name="homepage"),
    # path("signup", views.signup, name="signup")
]

