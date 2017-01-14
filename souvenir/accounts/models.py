#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models 

from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class MyProfile(UserenaBaseProfile):
	gender_choices = (
		('M', 'Male'),
		('F', 'Female'),
		('U', 'Unknown')
	)

	user = models.OneToOneField(User, 
		on_delete=models.CASCADE,
		unique=True,
		verbose_name=_('user'),
		related_name='my_profile')

	# 个人描述，微信的个性签名长度是 30 个字左右
	description = models.CharField(max_length=100)
	
	# 性别
	gender = models.CharField(max_length=1, choices=gender_choices, default='U')

	# 收到明信片的数量
	post_sent = models.IntegerField(default=0)  
	
	# 发出明信片的数量
	post_received = models.IntegerField(default=0)  
	
	# 等级
	level = models.IntegerField(default=1)

	def __str__(self):
		return self.user.username





