from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ckeditor.fields import RichTextField


from .choices import (
    StateInIndiaChoices, 
    CountryInWorldChoices, 
    VolunteeringForChoices,
    GetHelpForChoices
    )


class MetaInformation(models.Model):  
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,blank=True)
  
    class Meta:
        abstract = True


class ContactForm(models.Model):
    first_name = models.CharField(max_length=50, help_text="First Name", null=False, blank=False)
    last_name = models.CharField(max_length=50, help_text="Last Name", null=False, blank=False)
    email =models.EmailField(max_length=70, help_text="Email", null=True, blank=True)
    phone = models.CharField(max_length=10, help_text="Phone Number", null=False, blank=False)
    comments = models.CharField(max_length=200, help_text="Phone Number", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,blank=True)

class VolunteerMoodel(MetaInformation):
    first_name = models.CharField(max_length=50, help_text="First Name", null=False, blank=False)
    last_name = models.CharField(max_length=50, help_text="Last Name", null=False, blank=False)
    email =models.EmailField(max_length=70, help_text="Email", null=True, blank=True)
    phone = models.CharField(max_length=10, help_text="Phone Number", null=False, blank=False)
    volunteering_for =  models.CharField(
        max_length=100,
        choices=VolunteeringForChoices.choices,
        default=VolunteeringForChoices.ALL,
    )
    address = models.TextField(help_text="Address", null=True, blank=True)
    country = models.CharField(
        max_length=50,
        choices=CountryInWorldChoices.choices,
        default=CountryInWorldChoices.IN,
    )
    state = models.CharField(
        max_length=50,
        choices=StateInIndiaChoices.choices,
        default=StateInIndiaChoices.MH,
    )
    

class GetHelpModel(MetaInformation):
    first_name = models.CharField(max_length=50, help_text="First Name", null=False, blank=False)
    last_name = models.CharField(max_length=50, help_text="Last Name", null=False, blank=False)
    email = models.EmailField(max_length=70, help_text="Email", null=True, blank=True)
    phone = models.CharField(max_length=10, help_text="Phone Number", null=False, blank=False)
    get_help_for =  models.CharField(
        max_length=100,
        choices=GetHelpForChoices.choices,
        default=GetHelpForChoices.RHC,
    )
    address = models.TextField(help_text="Address", null=True, blank=True)
    country = models.CharField(
        max_length=50,
        choices=CountryInWorldChoices.choices,
        default=CountryInWorldChoices.IN,
    )
    state = models.CharField(
        max_length=50,
        choices=StateInIndiaChoices.choices,
        default=StateInIndiaChoices.MH,
    )



class ProjectsModel(MetaInformation):
    title = models.CharField(max_length=250, help_text="Project Title", null=False, blank=False)
    description = RichTextField()
    image = models.ImageField(upload_to ='uploads/% Y/% m/% d/', null=True, blank=True)
    short_url = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    meta_keywords = models.CharField(max_length=250, help_text="Meta Keywords", null=True, blank=True)	



class StoriesModel(MetaInformation):
    linked_project = models.ForeignKey(ProjectsModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, help_text="Project Title", null=False, blank=False)
    description = RichTextField()
    image = models.ImageField(upload_to ='uploads/% Y/% m/% d/', null=True, blank=True)
    short_url = models.SlugField(max_length=250, unique_for_date='publish')
    yt_url = models.CharField(max_length=300, help_text="Youtube Video Link", null=True, blank=True)
    fb_url = models.CharField(max_length=300, help_text="Facebook Link Page", null=True, blank=True)
    ig_url = models.CharField(max_length=300, help_text="Instagram Link Page", null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    meta_keywords = models.CharField(max_length=250, help_text="Meta Keywords", null=True, blank=True)	
    