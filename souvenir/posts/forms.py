from django.db import models
from django.forms import ModelForm
from django import forms

from .models import Post
from address.models import Country,District

from django.utils.translation import ugettext_lazy as _

import logging

logger = logging.getLogger(__name__)

provinces_set = District.objects.filter(code__regex = r'^..(0){4}$') | District.objects.filter(code = 0)
provinces_list = []
for district in provinces_set:
	c = {}
	logging.debug("[district.name] = " + district.name)
	c['value'] = district.code
	c['text'] = district.name
	provinces_list.append(c)


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ('post_title',
			'post_description',
			'post_quantity',
			'post_picture',
			'post_country',
			'post_province',
			'post_city',
			'post_district'
		)
		labels = {
			'post_title' : _('发片令标题'),
			'post_description' : _('描述'),
			'post_quantity' : _('发片数量'),
			'post_picture' : _('上传一张图片'),
			'post_country' : _('寄片的国家与地区'),
			'post_province' : _('寄片的省'),
			'post_city' : _('寄片的城市'),
			'post_district' : _('寄片的区县')
		}

	def __init__(self, *args, **kwargs):
	    super(PostForm, self).__init__(*args, **kwargs)
	    # 37 是中国的 在 address_country 表中的id，注意不是code
	    self.initial['post_country'] = 86
	    self.fields['post_country'].empty_label = "请选择"

	    self.fields["post_province"].queryset = provinces_set | District.objects.filter(code = 0) | District.objects.filter(code = -1)
	    self.fields['post_province'].empty_label = None
	    self.fields['post_province'].choices = provinces_list

	    self.fields["post_city"].queryset = District.objects.filter(code__regex = r'^.{4}(0){2}$') | District.objects.filter(code = 0)| District.objects.filter(code = -1)
	    self.fields['post_city'].empty_label = None
	    self.fields['post_city'].choices = []
	    
	    self.fields["post_district"].queryset = District.objects.filter(code__regex = r'(([1-9].)|(.[1-9]))$') | District.objects.filter(code = 0)
	    self.fields['post_district'].empty_label = None
	    self.fields['post_district'].choices = []