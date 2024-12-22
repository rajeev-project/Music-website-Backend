from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class Adduser(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email']
    

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song_name', 'artist_name', 'song_img', 'audio', 'title']