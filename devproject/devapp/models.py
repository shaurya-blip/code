from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    made_on = models.DateTimeField()
    body = models.TextField()

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('devapp.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    phone = models.CharField(max_length=75,blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("home")
