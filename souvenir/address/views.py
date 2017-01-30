from django.shortcuts import render
from django.http import HttpResponse

import json
# 引入正则表达式
import re

from .models import District

import logging
logger = logging.getLogger(__name__)

# Create your views here.

def getDistrictList(request):
	results = District.objects.none()
	
	code = request.GET.get('code', None)
	
	# logging.debug("[code] = " + str(code))

	# 选择了国家，如果是中国，列出所有中国的省
	if code == '86':
		# get all the provinces
		provinces = District.objects.filter(code__regex = r'(0){4}$') | District.objects.filter(code = 0)
		results = provinces
		# logging.debug("[view.BUG] = " + str(results.count()))
	
	elif len(code) == 6:
		# 如果选择是中国的某个省，则要返回市
		if re.match('[1-9].0{4}',code):
			# get all the cities in this province
			# 取字符串前两位
			province_code = code[0:2]
			city_regex = province_code+'(([1-9].)|(.[1-9]))0{2}'
			cities = District.objects.filter(code__regex = r''+city_regex) | District.objects.filter(code = 0)

			results = cities

		# 如果选择的是某个市，则要返回区
		if re.match('..(([1-9].)|(.[1-9]))0{2}',code):
			city_code = code[0:4]
			district_regex = city_code+'(([1-9].)|(.[1-9]))'
			districts = District.objects.filter(code__regex = r''+district_regex)| District.objects.filter(code = 0)

			if districts.count() == 1:
				province_code = code[0:2]
				district_regex = province_code+'..(([1-9].)|(.[1-9]))'
				districts = District.objects.filter(code__regex = r''+district_regex)| District.objects.filter(code = 0)
			
			results = districts
		else :
			# 别的情况不作处理，也没别的情况了
			# logging.debug("[code] = " + str(code))
			pass
	else:
		# 如果是别的国家，只返回 -1
		results = District.objects.filter(code = -1)
			
	list = []
	for district in results:
		c = {}
		c['name'] = district.name
		c['code'] = district.code
		list.append(c)
	
	# https://rayed.com/wordpress/?p=1508
	return HttpResponse(json.dumps(list),content_type = "application/json;charset=utf-8")
 