from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
# from datetime import date
# Create your models here.

class SaveQueries(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    question = models.CharField(null=False,max_length=2800) # jst limiting !!
    returnquery = models.CharField(null=False,max_length=35000)
    query_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question + " " + self.returnquery


