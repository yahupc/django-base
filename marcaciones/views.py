from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
# Create your views here.


def index(request):
    # return HttpResponse("<h1>Hello World</h1>")
    title = "DJANGO COURSE"
    return render(request,'index.html', {'title': title})

def about(request):
    #return HttpResponse("about")
    username = "YAHUPC"
    return render(request,'about.html',{'username': username})

def hello(request, username):
    return HttpResponse("<h1>Hello %s </h1> " % username)

def projects(request):
    projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)
    return render(request,'projects.html', {'projects': projects})

def tasks(request):
    # tasks = Task.objects.get(id=id)
    # tasks = get_object_or_404(Task, id=id)
    #return HttpResponse("tasks: %s" % tasks.title)
    #tasks = list(Task.objects.values())
    tasks = Task.objects.all()
    return render(request,'tasks.html',{'tasks': tasks})
