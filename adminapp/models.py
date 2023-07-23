from django.db import models


# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name
class Unversity(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(upload_to='images', null=True)
    region=models.ForeignKey(Region,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name
class Faculty(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    unversetit = models.ForeignKey(Unversity, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    kafedra = models.ForeignKey(Kafedra, null=True, on_delete=models.SET_NULL)


class Group(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images', null=True)
