from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Person(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    def __str__(self):
        return "fname="+self.fname+", lname="+self.lname

