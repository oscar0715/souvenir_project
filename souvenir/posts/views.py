from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.conf.urls import url
from django.views.generic import TemplateView, ListView,DetailView
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage


from .forms import PostForm
from address.models import Country, District
from .models import Post

import json
import logging

# 引入正则表达式
import re

logger = logging.getLogger(__name__)

@login_required(login_url='/accounts/signin/')
def newPost(request):

	if request.method == 'POST':
		# 获取当前用户
		current_user = request.user.my_profile
		form = PostForm(request.POST,request.FILES or None,instance=Post(user = current_user))
		if form.is_valid():
			# 创建一个 instance 但是不提交
			post = form.save(commit=False)
			# 可以在这里做一些改动
			post.card_left = form.cleaned_data['post_quantity']
			# 提交
			post.save()
			return HttpResponse('Thank you!')
		else:
			logging.debug("[view.BUG] = " + "wrong!")
	else: 
		form = PostForm()

	dictList = {
		'form':form,
	}
	return render(request,'posts/new.html',dictList)


def getDistrictList(request):
	list = []
	c = {}
	c['name'] = "请选择"
	c['code'] = 0
	list.append(c)
	
	code = request.GET.get('code', None)
	
	# 选择了国家，如果是中国，列出所有中国的省
	if code == '86':
		# get all the provinces
		provinces = District.objects.filter(code__regex = r'(0){4}$')

		# append to the list
		for province in provinces:
			c = {}
			c['name'] = province.name
			c['code'] = province.code
			list.append(c)

		# logging.debug("[view.BUG] = " + str(list.count()))
	
	elif len(code) == 6:
		# 如果选择是中国的某个省，则要返回市
		if re.match('[1-9].0{4}',code):
			# get all the cities in this province
			# 取字符串前两位
			province_code = code[0:2]
			city_regex = province_code+'(([1-9].)|(.[1-9]))0{2}'
			cities = District.objects.filter(code__regex = r''+city_regex)

			# logging.debug("[city_regex] = " + city_regex)
			# logging.debug("[cities.count()] = " + str(cities.count()))

			for city in cities:
				c = {}
				c['name'] = city.name
				c['code'] = city.code
				list.append(c)

		# 如果选择的是某个市，则要返回区
		if re.match('..(([1-9].)|(.[1-9]))0{2}',code):
			city_code = code[0:4]
			district_regex = city_code+'(([1-9].)|(.[1-9]))'
			districts = District.objects.filter(code__regex = r''+district_regex)

			if districts.count() == 0:
				province_code = code[0:2]
				district_regex = province_code+'..(([1-9].)|(.[1-9]))'
				districts = District.objects.filter(code__regex = r''+district_regex)
			
			# logging.debug("[district_regex] = " + district_regex)
			# logging.debug("[districts.count()] = " + str(districts.count()))

			
			for district in districts:
				c = {}
				c['name'] = district.name
				c['code'] = district.code
				list.append(c)
		else :
			# 别的情况不作处理，也没别的情况了
			# logging.debug("[code] = " + str(code))
			pass
	else:
		# 如果是别的国家，只返回 0
		logging.debug("Here2")
		del list[:]
		c = {}
		c['name'] = "------"
		c['code'] = 0
		list.append(c)
	
	# https://rayed.com/wordpress/?p=1508
	return HttpResponse(json.dumps(list),content_type = "application/json;charset=utf-8")


# List all of the Posts	
class IndexView(ListView):
	template_name = 'posts/index.html'
	context_object_name = 'posts'

	def get_queryset(self):
		return Post.objects.all()

# Detail of one chosen post
class DetailView(DetailView):
	model = Post
	template_name = 'posts/detail.html'
