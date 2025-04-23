from django.db import models
from django.contrib import admin
class Movie(models.Model):
    USER_ID = models.CharField(max_length=300,help_text='USER ID')
    USER_NAME = models.CharField(max_length=300)
    PHONE_NUMBER = models.IntegerField()
    EMAIL = models.EmailField()
    MOVIE_NAME = models.CharField(max_length=300)
    DATE = models.DateField()
    SHOW_TIME = models.TimeField()
    SEATS_Number= models.IntegerField()

class MovieAdmin(admin.ModelAdmin):
    list_display = ('USER_ID', 'USER_NAME', 'PHONE_NUMBER', 'EMAIL', 'MOVIE_NAME', 'DATE','SEATS_Number','SHOW_TIME')
