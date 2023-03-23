from django.db import models
from django.db.models import CheckConstraint, Q, F

# Create your models here.
class Credential(models.Model):
    email = models.CharField(primary_key=True, max_length=400)
    full_name= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    phone_no= models.IntegerField(max_length=11)


    def __str__(self):
        return self.full_name

class User(models.Model):
    post = models.ImageField(upload_to='static/images/', null=True, verbose_name="")

    profile = models.ForeignKey(Credential, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post)

class Comment(models.Model):
    comment = models.TextField()
    post= models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.post)

