from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.http import HttpResponse, Http404
from django.template import loader

from .models import Topic, Entry

# Create your views here.

#show all the topics which were created
def index(request):
    latest_topic_list = Topic.objects.order_by('-date_added')[:5]
    context = {
        'latest_topic_list': latest_topic_list
    }
    #we use render rather than: 
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'learning_logs/index.html', context)

#exibits the details of the topics
def detail(request, question_id):
    #using get_object_or_404
    question = get_object_or_404(Topic, id=question_id)
    entry = get_list_or_404(Entry, topic=question_id)
    return render(request, 'learning_logs/details.html', {'question': question, 'entry': entry})
#    #another option
#    try:
#        question = Topic.objects.get(id=question_id)
#    except Topic.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'learning_logs/details.html', {'question': question})
#    
#   #using just HttpResponse
#   return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Topic, id=question_id)
    entry = get_list_or_404(Entry, topic=question_id)
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)