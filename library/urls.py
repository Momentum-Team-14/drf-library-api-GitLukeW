from django.urls import path
from library import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('library/', views.BookList.as_view(), name='library-list'),
    path('library/<int:pk>/', views.BookDetail.as_view(), name='library-detail'),
    path('tracking/', views.TrackingList.as_view(), name='tracking-list'),
    path('<int:pk>/tracking/', views.TrackingDetail.as_view(), name='tracking-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
