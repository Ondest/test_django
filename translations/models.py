from django.urls import reverse
from django.db import models


class DictionaryModel(models.Model):
    word_1 = models.CharField(max_length=50)
    word_2 = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("form")
