from django.shortcuts import render
from django.http import HttpResponse
from userena.forms import (SignupForm, AuthenticationForm)

# Create your views here.

# http://stackoverflow.com/questions/31593972/how-to-return-django-form-object-in-an-ajax-request-from-django-template
# 获取一个form
def getSignInForm(request):
	# if request.method == 'Get':
	form = AuthenticationForm()
	return HttpResponse(form.as_p()) # return a html str