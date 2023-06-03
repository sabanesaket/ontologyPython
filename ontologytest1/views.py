from django.shortcuts import render

# Create your views here.
from django.conf import settings
# from django.contrib.auth.models import User
# from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import owlready2
from owlready2 import ThingClass

def getData():
    # Import the OWL ontology file.
    ontology = owlready2.get_ontology("C://Users//admin//ontologyPython//Final.owl").load()
    # print(ontology)

    # Parse the OWL ontology file.
    classes = ontology.classes()
    classesList = list(classes)
    # print(classesList)
    # print(type(classesList[2]))
    FAQClass = classesList[2]
    instances = FAQClass.instances()
    # print(instances)
    # for instance in instances:
    #     for question in instance.Question:
    #         print(question)
    #     for answer in instance.Answer:
    #         print(answer)
    # return instances
    mydict = {}
    for i in range(len(instances)):
        for j in range(len(instances[i].Question)):
            mydict[instances[i].Question[j]] = instances[i].Answer[j]
    # print(mydict)
    return mydict

def index(request):
    data = getData()
    print(data)
    # return HttpResponse(data)
    params = {'data':data}
    return render(request,'ontologytest1/index.html',params)


def about(request):
    return render(request, 'about.html')


