from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from time import time
import datetime

def gen_file(instance, filename):
    ext = filename.split('.')[-1]
    return '/static/corenxtimg/' + str(int(time())) + '.' + ext

class UserProfile(models.Model):
    """
    Custom user profile creation 'userprofile_userprofile'.when you click Delete This Stuff, the database record will be deleted and a signal will be sent to execute the img_post_delete_handler function. This will delete the image file from static/corenxtimg/.
    """
    feel = (
             ('Yippeee!','Yippeee!'),
             (':)',':)'),
             (':(',':('),
             ('\'SUP','SUP'),
             ('Kewl!','Kewl!'),
             ('BRB','BRB'),
             (':D',':D'),
             )

    year_in_school = (
                     ('Freshman','Freshman'),
                     ('Sophomore','Sophomore'),
                     ('Junior','Junior'),
                     ('Senior','Senior'),
                     )
    year_choices = []
    for r in range((datetime.datetime.now().year),(datetime.datetime.now().year+5)):
        year_choices.append((r,r))
    user = models.ForeignKey(User,unique=True)
    feel = models.CharField(max_length=10,null=True, choices=feel)
    pp = models.ImageField(upload_to=gen_file,default="/static/img/nxtwhite.jpg")
    school_name = models.CharField(max_length=50, default='High School')
    birth_date = models.DateField(blank=True, default=timezone.now)
    counselor_email = models.EmailField()
    year_in_school = models.CharField(max_length=15, choices=year_in_school, null=True,default="Freshman")
    interests = models.CharField(max_length=75)
    sports = models.CharField(max_length=75, null=True,blank=True)
    clubs = models.CharField(max_length=150, null=True)
    volunteer = models.CharField(max_length=350, null=True, blank=True)
    graduation_year = models.IntegerField(max_length=4, choices=year_choices,null=True) 
    User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


@receiver(post_delete, sender=UserProfile)
def img_post_delete_handler(sender, **kwargs):
    UserProfile = kwargs['instance']
    storage, path = Userprofile.pp.storage, Userprofile.pp.path
    storage.delete(path)
