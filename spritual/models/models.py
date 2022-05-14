from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ckeditor.fields import RichTextField

from .image_constant import image_497_x_499, image_382_by234, image_850_by_430

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

class EventModel(MetaInformation):
    title_name =  models.CharField(max_length=250, help_text="Title", null=False, blank=False)
    event_date =  models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=50, help_text="Location", null=False, blank=False)
    description = models.TextField(help_text="Description", null=True, blank=True)
    subtitle_name =  models.CharField(max_length=250, help_text="Sub Title", null=True, blank=True)
    subtitle_description = models.TextField(help_text="Subtitle Description", null=True, blank=True)
    photo = models.TextField(null=False, help_text="Photo(base64 encoded)",default=image_497_x_499) #base64 store of images
    event_detailed_pagephoto = models.TextField(null=False, help_text="Event Detailed Bottom Photo(base64 encoded)", default=image_382_by234) #base64 store of images
    event_banner_pagephoto = models.TextField(null=False, help_text="Event Detailed Banner(base64 encoded)", default=image_850_by_430) 
    
class ContactModel(models.Model):
    your_name = models.CharField(max_length=50, help_text="Your Name", null=False, blank=False)
    email =models.EmailField(max_length=70, help_text="Email", null=True, blank=True)
    phone = models.CharField(max_length=10, help_text="Phone Number", null=False, blank=False)
    subject = models.CharField(max_length=80, help_text="Subject", null=False, blank=False)
    comment = models.TextField(help_text="Your Message", null=True, blank=True)
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
    image = models.ImageField(upload_to ='uploads/%Y/%m/%d/', null=True, blank=True)
    short_url = models.SlugField(max_length=250, unique_for_date='publish')
    yt_url = models.CharField(max_length=300, help_text="Youtube Video Link", null=True, blank=True)
    fb_url = models.CharField(max_length=300, help_text="Facebook Link Page", null=True, blank=True)
    ig_url = models.CharField(max_length=300, help_text="Instagram Link Page", null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    meta_keywords = models.CharField(max_length=250, help_text="Meta Keywords", null=True, blank=True)	
    

class SiteInfoModel(MetaInformation):
    site_name = models.CharField(max_length=250, help_text="Site Name", null=False, blank=False)
    tag_line = models.CharField(max_length=250, help_text="Tag Line", null=True, blank=True)
    
    email = models.EmailField(max_length=70, help_text="Email", null=True, blank=True)
    phone = models.CharField(max_length=10, help_text="Phone Number", null=True, blank=True)

    alternate_phone_1 = models.CharField(max_length=10, help_text="Alternate Phone Numbe 1", null=True, blank=True)
    alternate_phone_2 = models.CharField(max_length=10, help_text="Alternate Phone Numbe 2", null=True, blank=True)
    alternate_phone_3 = models.CharField(max_length=10, help_text="Alternate Phone Numbe 3", null=True, blank=True)
    
    site_address = models.TextField(help_text="Site Address", null=True, blank=True)
    site_logo = models.ImageField(help_text="Site Logo", upload_to ='uploads/%Y/%m/%d/', null=True, blank=True)
    site_longitude_lattitude = models.CharField(max_length=250, help_text="Maps Location", null=True, blank=True)

    facebook_page =  models.CharField(max_length=300, help_text="Facebook Page", null=True, blank=True)
    instagram_page =  models.CharField(max_length=300, help_text="Instagram Page", null=True, blank=True)
    twitter_page =  models.CharField(max_length=300, help_text="Twitter Page", null=True, blank=True)
    linkedin_page =  models.CharField(max_length=300, help_text="LinkedIn Page", null=True, blank=True)
