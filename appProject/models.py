from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class product_sneakers(models.Model):
    product_name = models.CharField(max_length=40, null=False)
    product_description = models.CharField(max_length=130, null=False)
    product_price = models.IntegerField(null=False)
    product_image = models.ImageField(default='default.jpg', upload_to="profile_pics", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='sneakers')

    def total_likes(self):
        return self.likes.count()


class product_t_shirt(models.Model):
    product_name = models.CharField(max_length=40, null=False)
    product_description = models.CharField(max_length=130, null=False)
    product_price = models.IntegerField(null=False)
    product_image = models.ImageField(default='default.jpg', upload_to="profile_pics", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='t_shirts')

    def total_likes(self):
        return self.likes.count()


class product_hat(models.Model):
    product_name = models.CharField(max_length=40, null=False)
    product_description = models.CharField(max_length=130, null=False)
    product_price = models.IntegerField(null=False)
    product_image = models.ImageField(default='default.jpg', upload_to="profile_pics", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='hats')

    def total_likes(self):
        return self.likes.count()


class product_pant(models.Model):
    product_name = models.CharField(max_length=40, null=False)
    product_description = models.CharField(max_length=130, null=False)
    product_price = models.IntegerField(null=False)
    product_image = models.ImageField(default='default.jpg', upload_to="profile_pics", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='pants')

    def total_likes(self):
        return self.likes.count()


class product_football_sneakers(models.Model):
    product_name = models.CharField(max_length=40, null=False)
    product_description = models.CharField(max_length=130, null=False)
    product_price = models.IntegerField(null=False)
    product_image = models.ImageField(default='default.jpg', upload_to="profile_pics", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='football_sneakers')

    def total_likes(self):
        return self.likes.count()