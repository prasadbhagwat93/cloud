#from django.shortcuts import render
#from django import forms
# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
#from .models import Person
from django.core.exceptions import *
import os
import json
import requests
from urllib.request import urlopen
#from django.conf.settings import PROJECT_ROOT
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', contiext=None)

def search(request):
	if request.method == 'POST':
		#file_ = open(os.path.join(PROJECT_ROOT, 'filename'))
		search_id = request.POST.get('textfield', None)
		try:
			with open('/home/ec2-user/twitt1508084081.76') as f:
				content = f.readlines()
			content = [x.strip() for x in content]
			temp = []
			res = []
			for item in content:
				if "hazard" in str(item):
					temp.append(item)
			for i in temp:
				try:
					data = json.loads(str(i))
					url = "https://maps.googleapis.com/maps/api/geocode/json?address="
					location = str(data["user"]["location"]).split(",")
					loc = ""
					for j in location:
						loc = loc+j+"+"
					url = url+loc+"&key=AIzaSyCQk5ru6Y-42Z1kcsiae_O6oHBnDW_ib5w"
					response = json.loads(requests.get(url).text)
					lat_long = response["results"][0]["geometry"]["location"]
					res.append(str(lat_long))
				except Exception as e:
					res.append(str(e))
                			#print(lat_long)
	
			html = ("<H1>%s</H1>", str(res))
			#return HttpResponse(html)
			return render_to_response('map.html',{'test':res})
		except Person.DoesNotExist:
			return HttpResponse("no such user")  
	else:
		return render(request, 'form.html')

def index(request):
	return render(request, 'form.html')
