from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import foodItems # importing the class to get the item details stored in it, .models because same folder
from django.template import loader

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'templates.html'

def index(request):
    item_list = foodItems.objects.all()
    template = loader.get_template('tangyDjango/index.html')
    context = {
        #'item_list':item_list,
    }
    return HttpResponse(template.render(context, request)) # always two arguments, context and request
    # return HttpResponse("I have officially begun messing around :D")

def item(request):
    return HttpResponse("<h1> This isn't the index function </h1>")

def anotherPage(request):
    return HttpResponse("I made this page myself :)")


