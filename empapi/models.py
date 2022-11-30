from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.CharField(max_length = 3, primary_key = True)
    company_name = models.CharField(max_length = 100)



class Employee(models.Model):
    company = models.ForeignKey(Company,related_name = 'company',on_delete = models.CASCADE)
    fullname = models.CharField(max_length = 100)
    emp_code = models.CharField(max_length = 3)
    mobile = models.CharField(max_length = 15)
    