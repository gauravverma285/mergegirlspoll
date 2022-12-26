from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import apiview

urlpatterns = [
    path('post/', apiview.post_list),
    path('cat/', apiview.category_list),
    path('tag/', apiview.tag_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

