from django.db import models
from django.contrib import admin
class bankloan(models.Model):
	Name=models.CharField(max_length=20)
	Accountno=models.IntegerField(primary_key="Accountno")
	Amount=models.FloatField()
	DoB=models.DateField()
	Email=models.EmailField()
class bankloanAdmin(admin.ModelAdmin):
	list_display=('Name','Accountno','Amount','DoB','Email')
