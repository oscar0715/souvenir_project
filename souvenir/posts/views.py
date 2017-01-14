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

			# logging.debug("[city_regex] = " + city_regex)
			# logging.debug("[cities.count()] = " + str(cities.count()))

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
			logging.debug("[district_regex] = " + district_regex)
			logging.debug("[districts.count()] = " + str(districts.count()))
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
