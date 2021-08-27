from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Topic, Entry

# Create your views here.

#creating the first views!
def index(request):
    latest_topic_list = Topic.objects.order_by('-date_added')[:5]
    template = loader.get_template('learning_logs/index.html')
    context = {
        'latest_topic_list': latest_topic_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)