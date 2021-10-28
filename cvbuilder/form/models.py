from django.db import models

class Form(models.Model):
    picture = models.ImageField(blank=True, null=True, default="default.png")
    name = models.CharField(max_length=20, blank=True, null=True)
    surname = models.CharField(max_length=20, blank=True, null=True)
    date_of_bith = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    language1 = models.CharField(max_length=200, blank=True, null=True)
    language2 = models.CharField(max_length=200, blank=True, null=True)
    language3 = models.CharField(max_length=200, blank=True, null=True)
    skill1 = models.CharField(max_length=80, blank=True, null=True)
    skill2 = models.CharField(max_length=80, blank=True, null=True)
    skill3 = models.CharField(max_length=80, blank=True, null=True)
    skill4 = models.CharField(max_length=80, blank=True, null=True)
    skill5 = models.CharField(max_length=80, blank=True, null=True)
    skill6 = models.CharField(max_length=80, blank=True, null=True)
    previous_position = models.CharField(max_length=300, blank=True, null=True)
    education = models.CharField(max_length=300, blank=True, null=True)







