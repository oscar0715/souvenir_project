from django.db import models

from accounts.models import MyProfile

# Create your models here.
class District(models.Model):
	code = models.IntegerField(primary_key=True)
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name

class Country(models.Model):
	code = models.IntegerField(primary_key=True)
	country = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name 

class UserAddress(models.Model):
	user = models.ForeignKey(MyProfile, 
		on_delete=models.CASCADE)

	user_country = models.ForeignKey(Country,
		verbose_name ='国家')
	user_province = models.ForeignKey(District, 
		related_name='user_province',
		verbose_name ='省')
	user_city = models.ForeignKey(District, 
		related_name='user_city',
		verbose_name ='市')
	user_district = models.ForeignKey(District, 
		related_name='user_district',
		verbose_name ='区')

	detail_address = models.CharField(max_length=200, 
		blank = False,
		verbose_name ='详细地址')
	postcode = models.PositiveIntegerField(blank = False,
		verbose_name ='邮编')
	receiver_name = models.CharField(max_length=50,
		blank= False,
		verbose_name ='收信人')

	is_deleted = models.BooleanField(default = False) 

	def __str__(self):
		return self.receiver_name \
			+' '+self.user_country.name \
			+' '+self.user_province.name \
			+' '+self.user_city.name 

	def get_full_address(self):
		return self.user_country.name \
			+' '+self.user_province.name \
			+' '+self.user_city.name \
			+' '+self.user_district.name \
			+' '+self.detail_address \

		

