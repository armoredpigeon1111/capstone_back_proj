from django.contrib import admin
from .models import Fan, Musician
from .models import Gig
from .models import Review

# Register your models here.
admin.site.register(Musician)
admin.site.register(Gig)
admin.site.register(Review)
admin.site.register(Fan)