from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    """
    We need an author for each post, this will be the user who created the post, user is a separate table
    we will import the user module
    User is the related table
    What to do when the user is deleted, delete the post by the user
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
