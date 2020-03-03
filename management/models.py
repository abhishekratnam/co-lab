from django.db import models

class mentors(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email_id = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'mentor'
        verbose_name_plural = 'mentors'

    def __str__(self):
        return 'Email' + ' ' + str(self.email_id)


class students(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email_id = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
    def __str__(self):
        return 'Email' + ' ' + str(self.email_id)


    
