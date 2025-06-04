from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Song, FavoriteSong
from django.db.models import Q
from .forms import SongForm

# View to display all songs in the song list
@login_required(login_url='login')
def song_list(request):
    songs = Song.objects.all()
    search_query = request.GET.get('search', '')
    
    if search_query:
        songs = songs.filter(
            Q(title__icontains=search_query) |
            Q(artist__icontains=search_query) |
            Q(album__icontains=search_query)
        )
    
    return render(request, 'music_app/song_list.html', {
        'songs': songs,
        'search_query': search_query
    })

# View to handle adding a new song
@login_required(login_url='login')
def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save()
            messages.success(request, 'Song added successfully!')
            return redirect('song_detail', song_id=song.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SongForm()
    
    return render(request, 'music_app/add_song.html', {'form': form})

# View to delete a song
@login_required(login_url='login')
def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    song.delete()
    messages.success(request, 'Song deleted successfully!')
    return redirect('song_list')

# View to display favorite songs
@login_required(login_url='login')
def favorite_songs(request):
    favorites = FavoriteSong.objects.filter(user=request.user)
    return render(request, 'music_app/favorite_songs.html', {
        'favorites': favorites
    })

# View to toggle the favorite status of a song
@login_required(login_url='login')
def toggle_favorite(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if song.favorites.filter(id=request.user.id).exists():
        song.favorites.remove(request.user)
    else:
        song.favorites.add(request.user)
    return redirect('song_detail', song_id=song.id)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect('song_list')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'music_app/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'music_app/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'music_app/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'music_app/register.html')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('song_list')
    
    return render(request, 'music_app/register.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

@login_required(login_url='login')
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    is_favorite = song.favorites.filter(id=request.user.id).exists()
    
    return render(request, 'music_app/song_detail.html', {
        'song': song,
        'is_favorite': is_favorite
    })
