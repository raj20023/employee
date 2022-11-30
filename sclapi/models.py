from django.db import models
from django.db.models.fields import related

# Create your models here.
class student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length = 50)
    email_id = models.CharField(max_length = 50)
    parent_mobile_no = models.IntegerField(max_length = 10)
    gender = models.CharField(max_length = 10)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    date_of_join = models.DateField(auto_now=False, auto_now_add=False)
    delete = models.BooleanField(default = False)

class subject(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 1000)

class teacher(models.Model):
    name = models.CharField(max_length = 50)
    mobile_no = models.IntegerField(max_length = 10)
    email_id = models.EmailField(max_length=254)
    gender = models.CharField(max_length = 10)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    date_of_join = models.DateField(auto_now=False, auto_now_add=False)
    delete = models.BooleanField(default = False)
    subject = models.ForeignKey(subject,related_name = 'subject',on_delete = models.CASCADE)

class exam(models.Model):
    name = models.CharField(max_length = 50)
    date = models.DateField()
    type = models.CharField(max_length = 50)


class student_subject(models.Model):
    student_id = models.ForeignKey(student,related_name = 'student',on_delete = models.CASCADE)
    subject_id = models.ForeignKey(subject, related_name = 'stu_sub', on_delete = models.CASCADE)

class result(models.Model):
    stu_sub = models.ForeignKey(student_subject,related_name = 'stu_sub',on_delete = models.CASCADE)
    exam_id = models.ForeignKey(exam, related_name = 'exam', on_delete = models.CASCADE)
    score = models.CharField(max_length = 50)

