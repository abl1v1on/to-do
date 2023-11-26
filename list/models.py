from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Task(models.Model):
    task = models.CharField(max_length=200, verbose_name="Задача")
    status = models.ForeignKey("Status", on_delete=models.PROTECT, related_name="status",
                               verbose_name="Статус", default=1)
    user = models.ManyToManyField(User, related_name='user')

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('delete', kwargs={'pk': self.pk})


class Status(models.Model):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name
