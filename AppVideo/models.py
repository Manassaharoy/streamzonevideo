from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class streamVideo(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_uploader')
    title = models.CharField(max_length=50, verbose_name="Video title")
    videoURL = models.URLField(verbose_name="Video url(Embed link only for youtube)", null=True, blank=True)
    slug = models.SlugField(max_length=264, unique=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-upload_date',]

    def __str__(self):
        return self.title

class comments(models.Model):
    video = models.ForeignKey(streamVideo, on_delete=models.CASCADE, related_name='video_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField(verbose_name="Post a comment")
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date',]

    def __str__(self):
        return self.comment

class likes(models.Model):
    video = models.ForeignKey(streamVideo, on_delete=models.CASCADE, related_name='liked_video')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker_user')

    def __str__(self):
        return self.user + "likes" + self.video

