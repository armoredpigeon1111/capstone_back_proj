from django.db import models
from rest_framework import serializers
from .models import Musician
from .models import Review
from .models import Gig
from .models import Fan

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['id', 'username', 'bandname', 'genre', 'password']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'gig_id', 'body']

class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = ['id', 'musician_id', 'street', 'city', 'state', 'zipcode', 'likes', 'rsvps']

class FanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fan
        fields = ['id', 'username', 'password', 'genre1', 'genre2', 'genre3', 'zipcode']