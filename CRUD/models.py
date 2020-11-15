from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=40, null=True)
	number = models.CharField(max_length=40, null=True)
	
	def __str__(self):
		return self.name


