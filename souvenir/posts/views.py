from django.shortcuts import render,reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect


from .forms import PostForm
from .models import Post,CardClaim
from accounts.models import MyProfile

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

	def get_user(self):
		return self.request.user

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(DetailView, self).get_context_data(**kwargs)
		current_user = self.request.user.my_profile
		user_type = 0;
		if self.object.user == current_user:
			# 发布用户
			user_type = 1
		elif CardClaim.objects.filter(post=self.object, claimer=current_user).count()>0:
			# 已领取用户
			user_type = 2

		context['current_user_type'] = user_type
		logging.debug("[user_type] = " + str(user_type))
		return context

# 判断当前post下，当前用户是
# 0. 未领取
# 1. 发布者 
# 2. 已经领取
@login_required(login_url='/accounts/signin/')
def claim(request):
	if request.method == 'POST':
		post_id = request.POST.get('post_id', False)
		claimer_id = request.POST.get('claimer_id', False)

		post = Post.objects.get(pk=post_id)
		my_profile = MyProfile.objects.get(pk = claimer_id)

		if CardClaim.objects.filter(post=post,claimer=my_profile).count()>0:
			pass
		else:
			cardclaim = CardClaim.objects.create(post=post,claimer=my_profile)

			card_left = post.card_left - 1
			post.card_left = card_left
			post.save()

			return HttpResponseRedirect('/posts/'+post_id+"/")

# List all of the Posts of the user
class UserPostListView(ListView):
	template_name = 'posts/profile_userpost.html'
	context_object_name = 'posts'

	def get_queryset(self):
		return Post.objects.filter(user = self.request.user.my_profile)
