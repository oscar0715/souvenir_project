from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.http import HttpResponse


from .forms import PostForm
from .models import Post

import logging
logger = logging.getLogger(__name__)

@login_required(login_url='/accounts/signin/')
def newPost(request):

	if request.method == 'POST':
		# 获取当前用户
		current_user = request.user.my_profile
		form = PostForm(request.POST,request.FILES or None,instance=Post(user = current_user))
		
		# form.data['post_province'] = District.objects.get(code=form.data['post_province']).code
		# form.data['post_city'] = District.objects.get(code=form.data['post_city']).code
		# form.data['post_district'] = District.objects.get(code=form.data['post_district']).code
		# logging.debug("[view.is_valid_post_country] = " + form.data['post_country'])
		# logging.debug("[view.is_valid_post_province] = " + form.data['post_province'])
		# logging.debug("[view.is_valid_post_city] = " +form.data['post_city'])
		# logging.debug("[view.is_valid_post_district] = " + form.data['post_district'])

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
