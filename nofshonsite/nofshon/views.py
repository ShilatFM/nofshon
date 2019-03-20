from django.http import HttpResponse, Http404
from .models import Child, Disease
from django.shortcuts import render
import os
from django.template import loader
def home(request):
    return HttpResponse("hello")

def kids(request):
    # child_list = Child.objects.all()
    # output = ', '.join([q.child_name for q in child_list])+'\n'+'' +os.linesep+''.join([q.disease.name for q in child_list])
    # return HttpResponse(output)
    child_list = Child.objects.all()
    # template = loader.get_template('nofshon/kids.html')
    context = {
        'child_list': child_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'nofshon/kids.html', context)

def details(request, name):
    try:
        child = Child.objects.get(child_name=name)
    except Child.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'nofshon/details.html', {'child': child})
    # ch = Child.
    # answer = "details   " + name
    # return HttpResponse(answer)

