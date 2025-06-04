from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'release_date', 'cover_image', 'audio_file']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }