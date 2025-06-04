from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_audio_file(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp3', '.wav', '.ogg', '.m4a']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Please upload an audio file (MP3, WAV, OGG, or M4A).')

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200, blank=True)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    audio_file = models.FileField(
        upload_to='songs/',
        validators=[validate_audio_file],
        help_text='Upload an audio file (MP3, WAV, OGG, or M4A)'
    )
    favorites = models.ManyToManyField(User, related_name='favorite_songs', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"

    def clean(self):
        if not self.audio_file:
            raise ValidationError({'audio_file': 'An audio file is required.'})
        super().clean()

    class Meta:
        ordering = ['-created_at']

class FavoriteSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'song')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.song.title}"
