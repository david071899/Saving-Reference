from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import  render_to_response
from bs4 import BeautifulSoup
from django.template import RequestContext
import requests

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/collection_display/')
		
	username = request.POST.get('username')
	password = request.POST.get('password')

	user = auth.authenticate(username=username,password=password)

	if user is not None and user.is_active:
		auth.login(request,user)
		return HttpResponseRedirect('/collection_display/')

	else:
		return render_to_response('login.html',RequestContext(request,locals()))
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/login/')