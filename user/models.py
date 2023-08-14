from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    username = models.CharField(null=False,max_length=100)
    password=models.CharField(null=False,max_length=100)
    nickname=models.CharField(null=False,max_length=100)
    logintype=models.CharField(null=False,max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)