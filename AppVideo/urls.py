from django.contrib import admin
from django.urls import path, include


from AppVideo import views

app_name = "App_video"


urlpatterns = [
    path('', views.homepage.as_view(), name='homepage'),
    path('upload-video/', views.uploadVideo.as_view(), name='upload'),
    path('details/<slug:slug>', views.videodetails, name='videodetails'),
    path('liked/<pk>/', views.liked, name='liked_video'),
    path('unliked/<pk>/', views.unliked, name='unliked_video'),
    path('my-videos/', views.myUpload.as_view(), name='myupload'),
    path('edit/<pk>/', views.editUpload.as_view(), name='editupload'),
    path('delete/<pk>/', views.deleteVideo.as_view(), name='deletevideo'),
]
