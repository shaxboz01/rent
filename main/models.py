from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.urls import reverse


class About(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='media/',blank=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.FileField(upload_to='media/',blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('main:Blog', args=[self.title])

    class Meta:
        ordering = ('-date',)

class Car(models.Model):
    page_title = models.CharField(max_length=250, default='You will find a best car in our city')
    page_info = models.CharField(max_length=250, default='The best car is here')
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='media/',blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    phone_number = models.CharField(max_length=250)
    location = models.TextField()
    email = models.TextField()

    def __str__(self):
        return self.phone_number

class Advantages(models.Model):
    title = models.CharField(max_length=250)
    percent = models.CharField(max_length=250)
    speed = models.CharField(max_length=250)
    insurance = models.CharField(max_length=250)
    support = models.CharField(max_length=250)

    def __str__(self):
        return self.title