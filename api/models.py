from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    renda = models.FloatField()

    def __str__(self):
        return self.name


class Group(models.Model):
    code = models.PositiveIntegerField()
    users = models.ManyToManyField(User)
    taxa = models.FloatField()

    def __str__(self):
        return str(self.code)
