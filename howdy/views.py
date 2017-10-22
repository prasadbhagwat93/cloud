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
import urllib2
#from urllib.request import urlopen
#from django.conf.settings import PROJECT_ROOT
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', contiext=None)

def search(request):
	if request.method == 'POST':
		#file_ = open(os.path.join(PROJECT_ROOT, 'filename'))
		search_id = request.POST.get('textfield', None)
		try:
			with open('twitt1508098658.88') as f:
				content = f.readlines()
			content = [x.strip() for x in content]
			temp = []
			res = []
			for item in content:
				if search_id in str(item):
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
					response = json.load(urllib2.urlopen(url))
					lat_long = response["results"][0]["geometry"]["location"]
					res.append(lat_long)
				except Exception as e:
					#res.append(str(e))
					pass
                			#print(lat_long)
	
			hh="<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\"> <html xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:v=\"urn:schemas-microsoft-com:vml\"> \
  <head> <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\"/> <title>Google Maps JavaScript API Example: Simple Map</title> \
    <script src=\"http://maps.google.com/maps?file=api&amp;v=2&amp;sensor=false&amp\"\
 type=\"text/javascript\"></script> <script type=\"text/javascript\"> function initialize() {if (GBrowserIsCompatible()) {\
        var map = new GMap2(document.getElementById(\"map_canvas\"));\
        map.setCenter(new GLatLng(39.8163, -98.55762), 4);var point = new GLatLng(39.8163, -98.55762);"
	
			end="map.setUIToDefault();\
        map.addOverlay(new GMarker(point));} }</script> </head> <body onload=\"initialize()\" onunload=\"GUnload()\"> <div id=\"map_canvas\" style=\"width: 750px; height: 500px\"></div> </body> </html>"
			bar = []
			count = 0;
			for foo in res:
				hh = hh + "var point"+str(count)+" = new GLatLng("+str(foo["lat"])+","+str(foo["lng"])+");"
				end = "map.addOverlay(new GMarker("+"point"+str(count)+"));"+end
				count = count+1;
			return HttpResponse(hh+end)
			#return render_to_response('map.html',{'test':res})
		except:
			return HttpResponse("no such user")  
	else:
		return render(request, 'form.html')

def index(request):
	return render(request, 'form.html')
