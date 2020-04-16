from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.TextField(150)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class colabUser(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email_id = models.EmailField()
    mobile_no = models.IntegerField(max_length=20)
class menTors(models.Model):
    is_menTor = models.BooleanField(default=False)
    user = models.OneToOneField(colabUser,on_delete=models.CASCADE)#null=True , blank=True
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return "Name",self.user.fname+" "+self.user.lname+"  "+"Mentor",self.is_menTor
class stuDents(models.Model):
    is_stuDent = models.BooleanField(default=False)
    user = models.OneToOneField(colabUser,on_delete=models.CASCADE)#null=True , blank=True
    articles = models.ForeignKey(Articles,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return "Name", self.user.fname + " " + self.user.lname + "  " + "Mentor", self.is_stuDent



