from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
class collegelist(models.Model):
    """
      Custom addcollege model for students to add their choice of colleges.
      Every user can have more than 1 college in their list.
    """
    user = models.ForeignKey(User)
    college_name = models.CharField(max_length=100,null=True) 
     
    User.colleges = property(lambda u:collegelist.objects.filter(user=u)) 
