from django.db import models


class Post(models.Model):
	content = models.TextField("content")
	title = models.CharField("title", max_length=256)
	dateCreated = models.DateTimeField("date created", auto_now_add=True)
	videoURL = models.CharField("video URL", max_length=140)
    
	def __str__(self):
		return self.title