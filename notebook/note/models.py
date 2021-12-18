from django.db import models
# Create your models here.
from user.models import User


class Note(models.Model):
    title = models.CharField('title', max_length=100)
    content = models.TextField('content')
    created_time = models.DateTimeField('create_time', auto_now_add=True)
    updated_time = models.DateTimeField('update_time', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField('is_active', default=True)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.title, self.content, self.created_time, self.updated_time, self.user_id, self.is_active)
