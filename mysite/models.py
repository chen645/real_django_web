from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)#醉心時段update time zone

    def __str__(self):
        return self.title           #extract web title


class Country(models.Model):
    country_id = models.IntegerField()          #提示
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name        #return country's names


class City(models.Model):
    name = models.CharField(max_length=50)
    population = models.IntegerField()
    # country_id = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)      #say one number
    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title