from django.shortcuts import render
from home.models import Event, Project

# Create your views here.

def index(request):
    """A view of hoe page."""
    events = Event.objects.all()
    projects = Project.objects.all()
    context = {
        'events': events,
        'projects': projects  
    } 
    return render(request, 'index.html', context)

def about_us(request):
    events = Event.objects.all()
    projects = Project.objects.all()
    context = {
        'events': events,
        'projects': projects 
    } 
    return render(request, 'about_us.html', context)

def contact_us(request):
    events = Event.objects.all()
    projects = Project.objects.all()
    context = {
        'events': events,
        'projects': projects 
    } 
    return render(request, 'contact_us.html', context)

def login(request):
    events = Event.objects.all()
    projects = Project.objects.all()
    context = {
        'events': events,
        'projects': projects 
    } 
    return render(request, 'login.html', context)

def team(request):
    events = Event.objects.all()
    projects = Project.objects.all()
    context = {
        'events': events,
        'projects': projects 
    } 
    return render(request, 'team.html', context)

def event(request):
    events = Event.objects.all()
    projects = Project.objects.all()
    context = {
        'events': events,
        'projects': projects 
    } 
    return render(request, 'event.html', context)

def project(request, id):
    try:
        project = Project.objects.get(id=id)
        context = {
            'project': project
        } 
    except Exception as err:
        context = {}
    return render(request, 'project.html', context)


