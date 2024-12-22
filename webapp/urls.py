from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   path('home/',views.home,name='home'),
   path('playlist/',views.play,name='playlist'),
   path('podcast/',views.pod,name='podcast'),
   path('podpage/',views.podplay,name='page'),
   path('playlistpage/',views.listplay,name='playpage'),
   path('userin/',views.loginpage,name='login'),
   path('userout/',views.logoutpage,name='logout'),
   path('register/',views.registerpage,name='register'),
   path('okay/',views.okay),
   path('admin/',views.admin,name='admin'),
   path('songs/', views.song_list, name='song_list'),
   path('songs/add/', views.add_song, name='add_song'),
   path('songs/edit/<int:pk>/', views.edit_song, name='edit_song'),
   path('sections/', views.section_list, name='section_list'),
   path('sections/add/', views.add_section, name='add_section'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)