from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from forms import EventForm
from event.models import Event, Relation, Picture
# Create your views here.

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event=Event(title=form.cleaned_data['title'], start_date= form.cleaned_data['start_date'], end_date= form.cleaned_data['end_date'], user=request.user)
            event.save()
            for url in request.POST.getlist('attach'):
                gal = Picture(event=event,url=url)
                gal.save()
            return HttpResponseRedirect('/home')
    else:
        form = EventForm()
    variables = RequestContext(request, {'form':form})
    return render_to_response('event/event.html',variables)

def all_event(request):
    events= Event.objects.all().order_by('-create_date')
    return render(request, 'event/allevents.html', {"events":events})

def my_event(request):
    events = Event.objects.filter(user=request.user).order_by('-create_date')
    return render(request, 'event/allevents.html', {'events':events})

def attend(request,id):
    user = request.user
    event = Event.objects.get(id=id)
    events = Event.objects.all()
    variables = Relation(user=user, event=event)
    variables.save()
    return HttpResponseRedirect('/event/allevent')

def attending_event(request):
    events = [ i.event for i in Relation.objects.filter(user=request.user).order_by('-create_date')]
    return render(request, 'event/allevents.html', {'events':events})
