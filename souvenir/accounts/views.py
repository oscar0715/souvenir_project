from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView

from userena.forms import (SignupForm, AuthenticationForm)
from address.forms import UserAddressForm
from address.models import UserAddress

import logging
logger = logging.getLogger(__name__)


# Create your views here.

@login_required(login_url='/accounts/signin/')
def createAddress(request):
    if request.method == 'GET':
        form = UserAddressForm()
    else:
        current_user = request.user.my_profile
        form = UserAddressForm(request.POST,request.FILES or None,instance=UserAddress(user = current_user))

        if form.is_valid():
            # 创建一个 instance 但是不提交
            userAddress = form.save(commit=False)
            # 提交
            userAddress.save()
            return HttpResponseRedirect(reverse('accounts:address_added'))
        else:
            logging.debug("[view.BUG] = " + "wrong!")

    userAddresses = UserAddress.objects.filter(user=request.user.my_profile, is_deleted = False)
    
    dictList = {
        'form':form,
        'userAddresses' : userAddresses
    }
    return render(request,'accounts/profile_address.html',dictList)

@login_required(login_url='/accounts/signin/')
def createAddressComplete(request):
    
    userAddresses = UserAddress.objects.filter(user=request.user.my_profile, is_deleted = False)
    
    dictList = {
        'userAddresses' : userAddresses
    }
    return render(request,'accounts/profile_address_complete.html',dictList)

@login_required(login_url='/accounts/signin/')
def deleteAddress(request):
    address_id = int(request.GET["id"])
    UserAddress = UserAddress.objects.get(pk=address_id)
    UserAddress.is_deleted = True
    UserAddress.save()
    return HttpResponseRedirect(reverse('accounts:createAddress'))


# http://stackoverflow.com/questions/4673985/how-to-update-an-object-from-edit-form-in-django
@login_required(login_url='/accounts/signin/')
def editAddress(request,id):
    logging.debug("[view.BUG] = " + "editAddress")
    instance = get_object_or_404(UserAddress, id=id)
    form = UserAddressForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            logging.debug("[view.BUG] = " + "form.save()")
            return HttpResponseRedirect(reverse('accounts:createAddress'))
    return render(request, 'accounts/profile_address_edit.html', {'form': form} ) 
