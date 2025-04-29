from django.db import models

from django.contrib.auth.models import User

class Book(models.Model):
    objects = None
    title=models.CharField(max_length=255,null=False,blank=False)
    author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    def __str__(self):

        return self.title,self.author


