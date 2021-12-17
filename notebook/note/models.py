from django.db import models


# Create your models here.
from user.models import User


class Note(models.Model):
    title = models.CharField('title', max_length=100)
    content = models.TextField('content')
    created_time = models.DateTimeField('create_time', auto_now_add=True)
    updated_time = models.DateTimeField('update_time', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
