from django.db import models

# Create your models here.
class Musician(models.Model):
    username = models.CharField(max_length=50)
    bandname = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Gig(models.Model):
    musician_id = models.IntegerField(null=False)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    likes = models.IntegerField()
    rsvps = models.IntegerField()

class Review(models.Model):
    gig_id = models.IntegerField(null=False)
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.body
    
class Fan(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    genre1 = models.CharField(max_length=50)
    genre2 = models.CharField(max_length=50)
    genre3 = models.CharField(max_length=50)
    zipcode = models.IntegerField()
