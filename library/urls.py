from django.urls import path
from library import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('library/', views.BookList.as_view()),
    path('library/<int:pk>/', views.BookDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)