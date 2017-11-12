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

#from urllib.request import urlopen
#from django.conf.settings import PROJECT_ROOT
import boto3
from django.template import loader, Context
class HomePageView(TemplateView):
	def get(self, request, **kwargs):

		return render(request, 'index.html', contiext=None)


def search(request):
    if request.method == 'POST':
		#file_ = open(os.path.join(PROJECT_ROOT, 'filename'))
        search_id = request.POST.get('textfield', None)
        template = loader.get_template("map.html")
        try:
            client = boto3.client('sqs')
            queue_url = "https://sqs.us-east-1.amazonaws.com/ajfhjahafjahfjah/messi"
            response_value = client.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)
            message = response_value['Messages'][0]
            receipt_handle = message['ReceiptHandle']
            client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
            )
            tweet_text=message['MessageAttributes']['text']['StringValue']
            tweet_location = message['MessageAttributes']['twitter']['StringValue'].split(",")
            loc = ""
            url = "https://maps.googleapis.com/maps/api/geocode/json?address="

            for j in tweet_location:
                loc = loc+j+"+"
            url = url+loc+"&key=AIzaSyCQk5ru6Y-42Z1kcsiae_O6oHBnDW_ib5w"
            map_call = json.loads(requests.get(url).text)
            lat_long = map_call["results"][0]["geometry"]["location"]
            #tweet_location
            #output = template.render({"data":search_id})
            return HttpResponse(lat_long)
        except Exception as e:
            return HttpResponse("lol")
    else:
        return render(request, "form.html")
			#return render_to_response('map.html',{'test':res})

def index(request):
    return render(request, "form.html")
