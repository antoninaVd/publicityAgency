from django.db import models
from django.utils import timezone

class Article(models.Model):
	title = models.CharField(max_length=250)
	preview = models.TextField()
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	source = models.CharField(max_length=500)

def publish(self):
	self.date = timezone.now()
	self.save()

# Create your models here.
