from django.db import models
from django.forms import ModelForm
from django import forms

from .models import 
from address.models import Country,District

from django.utils.translation import ugettext_lazy as _

import logging

class UserAddressForm(ModelForm):
	class Meta:
		model = User_Address
		
		fields = ('user_country',
			'user_province',
			'user_city',
			'user_district',
			'detail_address',
			'postcode',
			'receiver_name')

	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		# 37 是中国的 在 address_country 表中的id，注意不是code
		self.initial['user_country'] = 86
		self.fields['user_country'].empty_label = "请选择"

		self.fields["user_province"].queryset = provinces_set | District.objects.filter(code = -1)
		self.fields['user_province'].empty_label = None
		# 上面的 queryset这个属性，是 validate 的选项们，是一个更大的区间范围
		# choices 这个属性就是初始可见的option列表
		# choices 属性不能直接用queryset作为input要转化为 select 可以接受的键值对
		# http://stackoverflow.com/questions/3429084/why-do-i-get-an-object-is-not-iterable-error
		self.fields['user_province'].choices = [(province.code,province.name) for province in provinces_set]

		self.fields["user_city"].queryset = District.objects.filter(code__regex = r'^.{4}(0){2}$') | District.objects.filter(code = 0)| District.objects.filter(code = -1)
		self.fields['user_city'].empty_label = None
		self.fields['user_city'].choices = []
		
		self.fields["user_district"].queryset = District.objects.filter(code__regex = r'(([1-9].)|(.[1-9]))$') | District.objects.filter(code = 0)
		self.fields['user_district'].empty_label = None
		self.fields['user_district'].choices = []