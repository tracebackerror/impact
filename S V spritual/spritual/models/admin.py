from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    search_fields = ['your_name', 'email', 'phone']
    
    list_display = ('id',
    'your_name', 'email','phone','subject','comment','created_date','modified_date')


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'campaign_hashlink',
        'campaign_heading',
        'campaign_donation_goal',
        'campaign_donation_raised',
        'campaign_donation_to_go',
        'image','created_date',
        'modified_date',
        )

@admin.register(FeaturedCampaign)
class FeaturedCampaignAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'feature_hashlink',
        'feature_heading',
        'feature_donation_goal',
        'feature_donation_raised',
        'feature_donation_to_go',
        'image','created_date',
        'modified_date',
        )

@admin.register(GetHelpModel)
class GetHelpModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone',
        
        )


@admin.register(ProjectsModel)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title','description','short_url','image','publish',
        'created_date',
        'modified_date'
        )
    prepopulated_fields = {'short_url': ('title',), }
    date_hierarchy = 'publish'
    empty_value_display = '-empty-'
    search_fields = ['title', 'description', 'meta_keywords', ]


@admin.register(StoriesModel)
class StoriesModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_date',
        'modified_date'
        )
    prepopulated_fields = {'short_url': ('title',), }
    date_hierarchy = 'publish'
    empty_value_display = '-empty-'
    search_fields = ['title', 'description', 'meta_keywords', ]
    
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    search_fields = ['first_name', 'last_name', 'email', 'phone']


@admin.register(SiteInfoModel)
class SiteInfoModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'site_name',
        'site_address',
        )
    
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    search_fields = ['site_name', 'email', 'address', ]


@admin.register(VolunteerModel)
class VolunteerModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email',
        'phone',
        'image','created_date',
        'modified_date',
        )
    
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    search_fields = ['first_name', 'last_name', 'email', 'phone']




