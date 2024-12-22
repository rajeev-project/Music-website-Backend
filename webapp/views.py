from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *

# Create your views here.
def home(req):
    cat1=Section.objects.get(id=1)
    s1=Song.objects.filter(title=1)
    cat2=Section.objects.get(id=2)
    s2=Song.objects.filter(title=2)
    cat3=Section.objects.get(id=3)
    s3=Song.objects.filter(title=3)
    return render(req, 'home.html',{'cat1':cat1,'cat2':cat2,'cat3':cat3,'s1':s1,'s2':s2,'s3':s3})

def play(req):
    sec1=Section1.objects.get(id=1)
    sec2=Section1.objects.get(id=2)
    sec3=Section1.objects.get(id=3)
    sec4=Section1.objects.get(id=4)
    pl1=Play.objects.filter(title=1)
    pl2=Play.objects.filter(title=2)
    pl3=Play.objects.filter(title=3)
    pl4=Play.objects.filter(title=4)
    return render(req, 'playlist.html',{'sec1':sec1,'sec2':sec2,'sec3':sec3,'sec4':sec4,'pl1':pl1,'pl2':pl2,'pl3':pl3,'pl4':pl4})

def pod(req):
    psec1=Section2.objects.get(id=1)
    psec2=Section2.objects.get(id=2)
    psec3=Section2.objects.get(id=3)
    pod1=Podc.objects.filter(title=1)
    pod2=Podc.objects.filter(title=2)
    pod3=Podc.objects.filter(title=3)
    return render(req, 'podcast.html',{'psec1':psec1,'psec2':psec2,'psec3':psec3,'pod1':pod1,'pod2':pod2,'pod3':pod3})


def podplay(req):
    pplay1=Podpage.objects.get(id=1)
    pplay2=Podpage.objects.get(id=2)
    pplay3=Podpage.objects.get(id=3)
    return render(req, 'podcastlink.html',{'pplay1':pplay1,'pplay2':pplay2,'psec3':pplay3})

def listplay(req):
    aplay1=Albumpage.objects.get(id=1)
    aplay2=Albumpage.objects.get(id=2)
    aplay3=Albumpage.objects.get(id=3)
    pic=Play.objects.get(id=1)
    return render(req, 'albumlink.html',{'aplay1':aplay1,'aplay2':aplay2,'aplay3':aplay3,'pic':pic})

def loginpage(req):
    user=req.POST.get('username')
    passw=req.POST.get('password')
    user=authenticate(req,username=user,password=passw)
    if user:
        login(req,user)
        messages.success(req,'user logged in successfully')
        return redirect(home)
    else:
        messages.error(req,'no such user')
    return render(req,'login.html')

def logoutpage(req):
    logout(req)
    messages.error(req,'user logged out successfully')
    return redirect(home)

def registerpage(request):
    if request.method == 'POST':     
        form=Adduser(request.POST)
        if form.is_valid():
            form.save()
            return redirect(loginpage)
    else:
        form=Adduser()
    return render(request,'register.html',{'form':form})

def okay(req):
    return render(req,'okay.html')

def admin(req):
    return render(req,'okay.html')


########################################################################

# View for listing songs
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})

# View for adding a new song
def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song_list')  # Redirect to song list after saving
    else:
        form = SongForm()
    return render(request, 'add_song.html', {'form': form})

# View for editing a song
def edit_song(request, pk):
    song = Song.objects.get(pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm(instance=song)
    return render(request, 'edit_song.html', {'form': form})

# View for creating a section
def add_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm()
    return render(request, 'add_section.html', {'form': form})


# View for listing  sections
def section_list(request):
    sections = Section.objects.all()
    return render(request, 'section_list.html', {'sections': sections})