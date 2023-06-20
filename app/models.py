from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_no=models.IntegerField()
    dept_name=models.CharField(max_length=100)
    dept_location=models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name
class Emp(models.Model):
    emp_no=models.IntegerField()
    e_name=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    mgr=models.IntegerField()
    Hiredate=models.DateField()
    salary=models.IntegerField()
    Dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.e_name

class Country(models.Model):
    c_no=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=100,unique=True)
class Capital(models.Model):
    ca_no=models.IntegerField(primary_key=True)
    c_name=models.OneToOneField(Country,on_delete=models.CASCADE)
    c_capital=models.CharField(max_length=100)
    