from django.db import models


class UserDetail(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    native = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    CGPA = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
