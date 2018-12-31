from django.db import models
from django.contrib.auth.models import User
#for the reverse url
from django.urls import reverse

# Create your models here.
DEFAULT_CATEGORY = 1

class Company(models.Model):
	name 		= models.CharField(max_length = 100)
	description = models.TextField(null = True)
	owner 		= models.ForeignKey(User, on_delete = models.CASCADE)
	latitude = models.CharField(max_length = 100, default = '27.624855')
	longitude = models.CharField(max_length = 100, default = '85.539744') 
	category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, default ='Cafe') 

	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# return reverse('company_list')
		#if want to redirect to its detail page then
		return reverse('company_detail' ,kwargs = {'pk' : self.pk})


class Category(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name