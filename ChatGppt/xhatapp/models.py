from django.db import models

# Create your models here.

class SaveQueries(models.Model):
    question = models.CharField(null=False,max_length=2800) # jst limiting !!
    returnquery = models.CharField(null=False,max_length=35000)

    def __str__(self):
        return self.question + " " + self.returnquery

