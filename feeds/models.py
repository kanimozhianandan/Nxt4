from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from time import time
import datetime

def genvideo_file(instance, filename):
    ext = filename.split('.')[-1]
    return '/static/corenxtvid/' + str(int(time())) + '.' + ext

class Feeds(models.Model):
    post_to = (
              ('Students','Students'),
              ('Counselors','Counselors'),
              ('Everyone','Everyone'),
              ) 
    user = models.ForeignKey(User) 
    feed = models.CharField(max_length=1050) 
    postdate = models.DateTimeField(default=datetime.datetime.now,null=True)
    video = models.FileField(upload_to="",null=True,blank=True)
    adddate = models.DateField(default=datetime.date.today,blank=True)
    postto = models.CharField(max_length=15,choices=post_to,null=True)

    User.post = property(lambda u: Feeds.objects.get_or_create(user=u)[0])
    User.posts = property(lambda u: Feeds.objects.filter(user=u))
    User.imgposts = property(lambda u: Feeds.objects.filter(video__iendswith='jpg'))


