from django.db import models

class Mentors(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email_id = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {} - {}".format(self.email_id, self.last_name,self.first_name)

class Students(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email_id = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {} - {}".format(self.email_id, self.last_name,self.first_name)


    
