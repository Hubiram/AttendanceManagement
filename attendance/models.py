# models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='subjects')

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    attended = models.BooleanField(default=False)
