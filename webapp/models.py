from django.db import models

# Create your models here.
class Section(models.Model):
    title=models.CharField(max_length=200)


    def __str__(self):
                return self.title

class Song(models.Model):
    song_name=models.CharField(max_length=200)
    artist_name=models.CharField(max_length=200)
    song_img=models.ImageField(upload_to='songsimg')
    audio = models.FileField(upload_to='audio_files/')
    title =models.ForeignKey(Section,on_delete=models.CASCADE)


    def __str__(self):
                return self.song_name

class Section1(models.Model):
    title=models.CharField(max_length=200)


    def __str__(self):
                return self.title

class Play(models.Model):
    song_name=models.CharField(max_length=200)
    artist_name=models.CharField(max_length=200)
    play_img=models.ImageField(upload_to='playsimg')
    title =models.ForeignKey(Section1,on_delete=models.CASCADE)


    def __str__(self):
                return self.song_name
    
class Section2(models.Model):
    title=models.CharField(max_length=200)


    def __str__(self):
                return self.title

class Podc(models.Model):
    song_name=models.CharField(max_length=200)
    artist_name=models.CharField(max_length=200)
    pod_img=models.ImageField(upload_to='podimg')
    title =models.ForeignKey(Section2,on_delete=models.CASCADE)


    def __str__(self):
                return self.song_name
    
class Podpage(models.Model):
    des=models.TextField()
    date=models.IntegerField()
    artist_name=models.CharField(max_length=200)
    ep_name=models.CharField(max_length=200)
    song_name =models.ForeignKey(Podc,on_delete=models.CASCADE)


class Albumpage(models.Model):
    song_name=models.CharField(max_length=200)
    date=models.IntegerField()
    artist_name=models.CharField(max_length=200)
    p_name =models.ForeignKey(Play,on_delete=models.CASCADE)
