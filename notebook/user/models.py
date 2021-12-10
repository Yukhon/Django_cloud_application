from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField('username', max_length=50, unique=True)
    password = models.CharField('password', max_length=32)
    create_time = models.DateTimeField('create_time', auto_now_add=True)
    updated_time = models.DateTimeField('last updated time', auto_now=True)
    update = 124

    def __str__(self):
        return '%s %s %s %s' % (self.username, self.password, self.create_time, self.updated_time)
