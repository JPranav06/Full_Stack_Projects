from django.db import models


class BlogModel(models.Model):
    # fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UserDetail(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    native = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    CGPA = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
