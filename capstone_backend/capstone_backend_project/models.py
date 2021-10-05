from django.db import models

# Create your models here.
class Musician(models.Model):
    musician_id = models.IntegerField()
    username = models.CharField(max_length=50)
    bandname = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Gig(models.Model):
    gig_id = models.IntegerField()
    musician_id = models.IntegerField(null=False)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    zipcode = models.IntegerField(max_length=15)
    likes = models.IntegerField(max_length=10)
    rsvps = models.IntegerField(max_length=10)

class Review(models.Model):
    review_id = models.IntegerField()
    gig_id = models.IntegerField(null=False)
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.body
