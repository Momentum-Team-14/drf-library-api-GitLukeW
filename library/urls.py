from django.urls import path
from library import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('library/', views.BookList.as_view(), name='library-list'),
    path('library/<int:pk>/', views.BookDetail.as_view(), name='library-detail'),
    path('library/featured/', views.FeaturedBook.as_view(), name='featured_book'),
    path('tracking/', views.TrackingList.as_view(), name='tracking-list'),
    path('tracking/<int:pk>/', views.TrackingDetail.as_view(), name='tracking-detail'),
    path('notes/', views.NoteList.as_view(), name='notes-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='notes-detail'),
    path('notes/all/', views.PublicNote.as_view(), name="all_notes_list"),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
