from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.urls import reverse

class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone_number:
            raise ValueError("Users must have an email address")

        user = self.model(
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone_number=phone_number,
            password=password,
        )
        user.is_staff=True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
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