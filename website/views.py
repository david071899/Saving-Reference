from django.shortcuts import  render_to_response
from bs4 import BeautifulSoup
from urlparse import urlparse
from django.template import RequestContext
import requests
import json
from website.models import Tag,Art,Collection
from collections import Counter
from django.contrib import auth
from django.http import HttpResponseRedirect
# Create your views here.

def crawler(request):
	if request.user.is_authenticated():
		if request.POST:				
			url=request.POST['url']
			key =urlparse(url)
			all_links=[]
			all_src=[]

			if key.netloc=="www.behance.net":
				header_info = {
					'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
					'Host':'www.behance.net',
					'Connection':'keep-alive',
					'cookie':'ilo0=true',
					}
				res=requests.get(url,headers=header_info)
				soup = BeautifulSoup(res.text.encode("utf-8"),"html.parser")
				title = soup.find('div', {'id':'project-name'}).text
				for pic in soup.find_all("img"):
					try:
						#print pic['src']
						all_links.append(pic['src'])
					except:
						pass
					try:
						#print pic['data-src']
						all_links.append(pic['data-src'])
					except:
						pass
				for item in all_links:
					for  part in item.split("/"):
						if part=='project_modules':
							all_src.append(item)

			else:
				res = requests.get(url)
				soup = BeautifulSoup(res.text.encode("utf-8"))
				title = ''
				for item in  soup.find_all("img"):
					all_links.append(item['src'])

				for i in all_links:
					if i[0]=="h":
						all_src.append(i)

		return render_to_response('crawler.html',RequestContext(request,locals()))
	else:
		return HttpResponseRedirect("/login/")	

def select(request):

	if request.POST:
		url_select=request.POST.getlist('select')

	return render_to_response('select.html',RequestContext(request,locals()))

def  ending(request):
	if request.user.is_authenticated():
		if request.POST:
			
			name=request.POST['name']
			style=request.POST['style'].split(",")
			description=request.POST['description']
			pic_url=request.POST['pic_url']
			
			if Art.objects.get(name=name):
				warning=" Name Conflict , Please change the name "
				return render_to_response('Wrong_naming.html',RequestContext(request,locals()))
			else:
				Art.objects.create(
					name=name,
					adder=request.user,
					)
				Tag.objects.create(
					style=style,
					description=description,
					pic_url=pic_url,
					art=Art.objects.get(name=name),
					)
				return render_to_response('Add_Success.html',RequestContext(request,locals()))
			
		return render_to_response('Add_Success.html',RequestContext(request,locals()))
	else:
		return HttpResponseRedirect("/login/")	

def display(request):
	if request.user.is_authenticated():
		user=request.user
		total=[]
		account_list=[]
		
		art_all=Art.objects.all()

		for i in art_all:
			for  style in i.tag_set.all()[0].style:
				total.append(style)

		account=sorted(Counter(total).iteritems() , key=lambda x : x[1] , reverse=True)

		for key in account:
			temp=[key[0],key[1]]
			account_list.append(temp)
		top5=account_list[0:5]

		#return render_to_response('collection_display.html',RequestContext(request,locals()))

		
		if request.POST:
			name_collection=request.POST['getcollection']
			Collection.objects.get_or_create(collecter=request.user,defaults={'collecter':request.user})
			Art.objects.update_or_create(name=name_collection,defaults={'collecter':Collection.objects.filter(collecter=request.user)})


			return render_to_response('collection_display.html',RequestContext(request,locals()))
		
		return render_to_response('collection_display.html',RequestContext(request,locals()))

	else:
		return HttpResponseRedirect("/login/")


def  profile(request):
	if   request.user.is_authenticated():
		Collection.objects.get_or_create(collecter=request.user,defaults={'collecter':request.user})
		user=request.user
		user_collection=user
		art_user_add=request.user.art_set.all()
		art_user_collection=request.user.collection.art_set.all()
		return render_to_response('profile.html',RequestContext(request,locals()))
	else:
		return HttpResponseRedirect("/login/")






