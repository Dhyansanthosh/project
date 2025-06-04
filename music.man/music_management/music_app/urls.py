from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('songs/<int:song_id>/', views.song_detail, name='song_detail'),
    path('songs/add/', views.add_song, name='add_song'),
    path('favorites/', views.favorite_songs, name='favorite_songs'),
    path('songs/<int:song_id>/toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('songs/<int:song_id>/delete/', views.delete_song, name='delete_song'),
]
