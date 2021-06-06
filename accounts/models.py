from django.db import models

# Create your models here.
class Register(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.charField(max_length=50)
    username = models.charField(max_length=50)
    emailid = models.models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)