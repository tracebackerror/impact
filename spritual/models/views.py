import imp
from django.shortcuts import render
from .forms import ContactForm, CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
import json
import base64
from django import forms    



from .models import (ContactModel, 
                     EventModel,
                     BlogModel
                     )

# Create your views here.
def index(request):
    return render(request, 'models/index.html')

def about(request):
    return render(request, 'models/about.html')

def blog_details(request, blog_id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
           
            instance=comment_form.save(commit=False)
            instance.blog = BlogModel.objects.get(id=blog_id)
            instance.save()
            
      
            
    blog_object = BlogModel.objects.get(id=blog_id)
    if blog_object.tags and isinstance(blog_object.tags, str):
        blog_object.tag_separated = blog_object.tags.split(",")
        blog_object.tag_separated = [each_tag.strip() for each_tag in  blog_object.tag_separated ]
        
    recent_blog = BlogModel.objects.all().only('blog_title').order_by("-created_date")[:3] 
    return render(request, 
                  'models/blog_details.html', 
                  {
                      'blog_object': blog_object,
                      'recent_blog': recent_blog
                   })

def blog(request):
    blog_all = BlogModel.objects.all().order_by("-created_date")
    recent_blog = BlogModel.objects.all().only('blog_title').order_by("-created_date")[:3]
    return render(request, 
                  'models/blog.html', 
                  {
                      'blog_all': blog_all,
                      'recent_blog': recent_blog
                   })

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