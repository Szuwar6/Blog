from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
