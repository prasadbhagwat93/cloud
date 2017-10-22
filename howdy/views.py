#from django.shortcuts import render
#from django import forms
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
#from .models import Person
from django.core.exceptions import *
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', contiext=None)

def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            #user = Person.objects.get(name = search_id)
            #do something with user
            html = ("<H1>%s</H1>", search_id)
            return HttpResponse(html)
        except Person.DoesNotExist:
            return HttpResponse("no such user")  
    else:
        return render(request, 'form.html')

def index(request):
    return render(request, 'form.html')
