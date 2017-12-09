#from django.shortcuts import render
#from django import forms
# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
#from django.shortcuts import render_templete
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
#from .models import Person
from django.core.exceptions import *
import os
import json
import requests
import ast
#from urllib.request import urlopen
#from django.conf.settings import PROJECT_ROOT
import boto3
from django.template import loader, Context

lat = 0
lon =0
class HomePageView(TemplateView):
	def get(self, request, **kwargs):

		return render(request, 'index.html', contiext=None)


def search(request):
    global lat
    global lon
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        if(search_id == ''):
            send_url = 'http://freegeoip.net/json'
            r = requests.get(send_url)
            j = json.loads(r.text)
            lat = j['latitude']
            lon = j['longitude']
            return HttpResponse(str(lat))

        else:
            new_url = "https://maps.googleapis.com/maps/api/geocode/json?address="+search_id+"&key=AIzaSyCqk2xG-5-v6vm4xB8q-4UwuYyNoL-b6L4"
            ans = requests.get(new_url).json()
            #ans = json.loads(ans)
            #at = ans['results'][0]['geometry']['location']['lat']
            lat = ans["results"][0]["geometry"]["location"]["lat"]
            lon = ans["results"][0]["geometry"]["location"]["lng"]
            return HttpResponse()


def index(request):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    username = request.POST.get('login', None)
    password = request.POST.get('password', None)
    response = table.get_item(Key={'username': username},)
    item = response['Item']['password']
    if item == password:

        return render(request, "form.html")

    else:
        return HttpResponse("wrong passoword")

def locations(request):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response = table.get_item(Key={'username': 'fab'},)
    items = response['Item']['age']
    item = ast.literal_eval(items)
    context = {'data':str(item)}
    return render(request,'locations.html', context)

def items(request):
    return render(request, "itemManagement.html")

def add_items(request):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response = table.get_item(Key={'username': 'fab'},)
    item = response['Item']['age']
    item = ast.literal_eval(item)
    item.append(request.POST.get('textfield', None))

    #items = items+","+request.POST.get('textfield', None)
    table.update_item(Key={'username': 'fab'},UpdateExpression='SET age = :val1',ExpressionAttributeValues={':val1': str(item)})
    return HttpResponse(item)
    #pass


def delete_items(request):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response = table.get_item(Key={'username': 'fab'},)
    items = response['Item']['age']
    item = ast.literal_eval(items)
    try:
        item.remove(request.POST.get('textfield', None))
    except:
        pass
    update_item = ""
    table.update_item(Key={'username': 'fab'},UpdateExpression='SET age = :val1',ExpressionAttributeValues={':val1': str(item)})
    return HttpResponse("goo")


def view_items(request):
    return HttpResponse("goo")

def login(request):
   return render(request,'login.html')

def signup(request):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    username = request.POST.get('login', None)
    password = request.POST.get('password', None)
    list_ = []
    table.put_item(Item={'username': username,'password': password, 'items':str(list_)})
    return HttpResponse("successfull")
