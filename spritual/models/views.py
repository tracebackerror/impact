import imp
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
import json
import base64



from .models import (ContactModel, 
                     EventModel
                     )

# Create your views here.
def index(request):
    return render(request, 'models/index.html')

def about(request):
    return render(request, 'models/about.html')

def blog_details(request):
    return render(request, 'models/blog_details.html')

def blog(request):
    return render(request, 'models/blog.html')

def contact(request):
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return JsonResponse({'message': "Message Sent", 
                                 "success": "success"
            })
        else:
            return JsonResponse({
                'message': dict(contact_form.errors.items()),
            })
    return render(request, 'models/contact.html')

def donation_details(request):
    return render(request, 'models/donation_details.html')

def donation_listing(request):
    return render(request, 'models/donation_listing.html')

def event_details(request, event_id):
    event_object = EventModel.objects.get(id=event_id)
    return render(request, 'models/event_details.html', {'event_details': event_object})

def events(request):
    events_objects = EventModel.objects.all().order_by('-event_date')
    return render(request, 'models/events.html', {'all_events': events_objects})

def faq(request):
    return render(request, 'models/faq.html')

def product_details(request):
    
    return render(request, 'models/product_details.html')

def products(request):
    return render(request, 'models/products.html')

def service(request):
    return render(request, 'models/service.html')

def stories_details(request):
    return render(request, 'models/stories_details.html')

def stories(request):
    return render(request, 'models/stories.html')

def volunteers(request):
    return render(request, 'models/volunteers.html')