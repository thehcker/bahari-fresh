from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=150, blank=True)
	city = models.CharField(max_length=120,default='')
	phone = models.IntegerField(default=0)
	last_seen = models.DateTimeField(auto_now=True)
	description = models.TextField(max_length=150, blank=True, default="Enter your Products description")
	image = models.ImageField(upload_to='documents/',null=True,blank=True)

	def __unicode__(self):
		return self.user.username

def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile = Profile.objects.create(user=kwargs['instance'])

	post_save.connect(create_profile,sender=User)

	