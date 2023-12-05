from django.db import models
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField()
    keywords = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=255)

    descriptions = models.TextField()
    short_descriptions = models.TextField()

    account = models.ForeignKey(settings.AUTH_USER_MODEL)
    categories = models.ManyToManyField(Category)


