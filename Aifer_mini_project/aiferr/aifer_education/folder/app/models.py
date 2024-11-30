from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    education = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='blog_images/', blank=True, null=True)


    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    required_education = models.CharField(max_length=100)

    def __str__(self):
        return self.name
