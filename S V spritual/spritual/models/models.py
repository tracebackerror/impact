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
    your_name = models.CharField(max_length=50, help_text="Your Name", null=False, blank=False)
    email =models.EmailField(max_length=70, help_text="Email", null=True, blank=True)
    phone = models.CharField(max_length=10, help_text="Phone Number", null=False, blank=False)
    subject = models.CharField(max_length=80, help_text="Subject", null=False, blank=False)
    comment = models.CharField(max_length=200, help_text="Your Message", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True,blank=True)



class Campaign(MetaInformation):
    campaign_hashlink = models.CharField(max_length=50, help_text="Hashlink of featured campaign e.g. Life, Food, Education etc.",)
    campaign_heading = models.CharField(max_length=100, help_text="Heading of featured campaign",)
    campaign_description = models.CharField(max_length=100, help_text="Description of featured campaign",)
    campaign_donation_goal = models.PositiveIntegerField(default=1)
    campaign_donation_raised = models.PositiveIntegerField(default=1)
    campaign_donation_to_go = models.PositiveIntegerField(default=1)
    campaign_bar_data = models.PositiveIntegerField(default=1,help_text="Maximum bar size 100")
    image = models.ImageField(upload_to ='campaign_image',help_text="resolution of 552x310",)

class FeaturedCampaign(MetaInformation):
    feature_hashlink = models.CharField(max_length=50, help_text="Hashlink of featured campaign e.g. Life, Food, Education etc.",)
    feature_heading = models.CharField(max_length=100, help_text="Heading of featured campaign",)
    feature_description = models.CharField(max_length=100, help_text="Description of featured campaign",)
    feature_donation_goal = models.PositiveIntegerField(default=1)
    feature_donation_raised = models.PositiveIntegerField(default=1)
    feature_donation_to_go = models.PositiveIntegerField(default=1)
    feature_bar_data = models.PositiveIntegerField(default=1,help_text="Maximum bar size 100")
    image = models.ImageField(upload_to ='featured_campaign_image',help_text="resolution of 400x225",)

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
    image = models.ImageField(upload_to ='main_project_image', null=True, blank=True)
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

class VolunteerModel(MetaInformation):
    full_name = models.CharField(max_length=70, help_text="Full Name", null=False, blank=False)
    email =models.EmailField(max_length=70, help_text="Email",)
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
    fb_url = models.CharField(max_length=300, help_text="Facebook Link Page", null=True, blank=True)
    tw_url = models.CharField(max_length=300, help_text="Twitter Link Page", null=True, blank=True)
    ig_url = models.CharField(max_length=300, help_text="Instagram Link Page", null=True, blank=True)
    li_url = models.CharField(max_length=300, help_text="Linkedin Link Page", null=True, blank=True)
    image = models.ImageField(upload_to ='volunteers_image', help_text="resolution of 256x258", null=True, blank=True)
    

