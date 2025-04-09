from django.db import models
from django.urls import reverse


class Status(models.Model):
    status_text = models.CharField(max_length=20)

    def __str__(self):
        return self.status_text


class List(models.Model):
    list_text = models.CharField(max_length=30)

    def __str__(self):
        return self.list_text


class Task(models.Model):
    shorttext = models.CharField(max_length=140)
    longtext = models.TextField(blank=True)
    till_when_date = models.DateField(verbose_name="till when")
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    list_items = models.ForeignKey(List, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.shorttext

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id', self.id})
