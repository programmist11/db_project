from django.db import models
from django.conf import settings
from django.utils import timezone

from src.apps.article.models import Article

import uuid
from datetime import timedelta


REACTION_CHOICES = (
    ('+', 'Лайк'),
    ('-', 'Дизлайк'),
)


def end_date():
    return timezone.now() + timedelta(minutes=30)


class ConfirmEmail(models.Model):
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    end_date = models.DateTimeField(default=end_date)


class ArticleViewed(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    session = models.CharField(max_length=255)

    add_date = models.DateTimeField(auto_now_add=True)


class ArticleReaction(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    reaction = models.CharField(max_length=1, choices=REACTION_CHOICES)

    add_date = models.DateTimeField(auto_now_add=True)


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    text = models.CharField(max_length=500)

    add_date = models.DateTimeField(auto_now_add=True)
