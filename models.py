from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Book( models.Model):
    title = models.CharField( max_length=40);
    description = models.CharField( max_length=100); 
    price = models.DecimalField( max_digits=6, decimal_places=2);

class Person(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.IntegerField()
    def __str__(self):
        return "fname="+self.fname+", lname="+self.lname+", age="+self.age

class Account(models.Model):
    username = models.CharField( max_length=30)
    password = models.CharField( max_length=30)
    displayname = models.CharField( max_length=30)
    def __str__( self):
        return "{}, {}, {}".format( self.username, self.password, self.displayname)
