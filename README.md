# Ex02 Django ORM Web Application
## Date:26.10.24 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from django.contrib import admin
from .models import Student,StudentAdmin
admin.site.register(Student,StudentAdmin)
models.py
from django.db import models
from django.contrib import admin
class Student(models.Model):
	Name=models.CharField(max_length=20)
	Accountno=models.IntegerField(primary_key="Accountno")
	Amount=models.FloatField()
	DoB=models.DateField()
	Email=models.EmailField()
class StudentAdmin(admin.ModelAdmin):
	list_display=('Name','Accountno','Amount','DoB','Email')
    ```

## OUTPUt
Screenshot (1).png
c:\Users\Admin\ORM\Screenshot (2).png


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
