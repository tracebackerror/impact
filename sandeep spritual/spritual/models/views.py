from django.shortcuts import render
from django.views import View
from .models import MetaInformation,ContactForm,VolunteerMoodel,GetHelpModel,ProjectsModel,StoriesModel,SiteInfoModel,FeaturedCampaign

# Create your views here.
# def index(request):
#     return render(request, 'models/index.html')

class indexview(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        feature = FeaturedCampaign.objects.all()

        return render(request, 'models/index.html',{'project':project,'feature':feature})

# def about(request):
#     return render(request, 'models/about.html')

class aboutview(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/about.html',{'project':project})


class blog_details_view(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/blog_details.html',{'project':project})

class blogview(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/blog.html',{'project':project})

class contactview(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/contact.html',{'project':project})

class donation_details_view(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/donation_details.html',{'project':project})

class donation_listing_view(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/donation_listing.html',{'project':project})

class event_details_view(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/event_details.html',{'project':project})

class eventsview(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/events.html',{'project':project})

class faqview(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/faq.html',{'project':project})

class product_details_view(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/product_details.html',{'project':project})

class productsview(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/products.html',{'project':project})

class serviceview(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/service.html',{'project':project})

class stories_details_view(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/stories_details.html',{'project':project})

class storiesview(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/stories.html',{'project':project})

class volunteersview(View):
    def get(self, request):
        project = ProjectsModel.objects.all()
        return render(request, 'models/volunteers.html',{'project':project})