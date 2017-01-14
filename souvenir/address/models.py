from django.db import models

from accounts.models import MyProfile



# Create your models here.
class District(models.Model):
	code = models.IntegerField()
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name

class Country(models.Model):
	country = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	code = models.IntegerField()
	def __str__(self):
		return self.name

# default country list
countries = Country.objects.all()
COUNTRY_CHOICES = []
for country in countries:
	COUNTRY_CHOICES.append([country.code,country.name])

class User_Address(models.Model):
	user = models.ForeignKey(MyProfile, on_delete=models.CASCADE)

	country = models.IntegerField(choices=COUNTRY_CHOICES)
	province = models.IntegerField()
	city = models.IntegerField()
	district = models.IntegerField()
	detail_address = models.CharField(max_length=200, blank = False)
	postcode = models.PositiveIntegerField(blank = False)
	receiver_name = models.CharField(max_length=50,blank= False)

	def __str__(self):
		return self.receiver_name

