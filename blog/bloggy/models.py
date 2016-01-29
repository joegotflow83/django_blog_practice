from django.db import models
from datetime import datetime

# Create your models here.
class Users(models.Model):

	
	username = models.CharField(max_length=30, blank=False)
	password = models.CharField(max_length=20, blank=False)


class Posts(models.Model):

	title = models.CharField(max_length=30)
	post = models.CharField(max_length=150)
	date = models.DateField(default=datetime.now)

	def __unicode__(self):

		return self.title