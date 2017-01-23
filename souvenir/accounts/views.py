from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from userena.forms import (SignupForm, AuthenticationForm)
from address.forms import UserAddressForm
from address.models import User_Address

import logging
logger = logging.getLogger(__name__)


# Create your views here.

@login_required(login_url='/accounts/signin/')
def createAddress(request):
	if request.method == 'GET':
		form = UserAddressForm()
	else:
		current_user = request.user.my_profile
		form = UserAddressForm(request.POST,request.FILES or None,instance=User_Address(user = current_user))

		if form.is_valid():
			# 创建一个 instance 但是不提交
			user_address = form.save(commit=False)
			# 提交
			user_address.save()
			return HttpResponseRedirect(reverse('accounts:createAddress'))
		else:
			logging.debug("[view.BUG] = " + "wrong!")

	user_addresses = User_Address.objects.filter(user=request.user.my_profile)
	
	dictList = {
		'form':form,
		'user_addresses' : user_addresses
	}
	return render(request,'accounts/profile_address.html',dictList)

@login_required(login_url='/accounts/signin/')
def deleteAddress(request):
	address_id = int(request.GET["id"])
	User_Address.objects.get(pk=address_id).delete()


	return HttpResponseRedirect(reverse('accounts:createAddress'))
		
