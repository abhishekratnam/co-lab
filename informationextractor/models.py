from django.db import models

# Create your models here.
class Data(models.Model):
    fname = models.TextField()
    lname = models.TextField()
    email = models.TextField()

    def __str__(self):
        return self.fname+ ' '+ self.lname    