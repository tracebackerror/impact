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


@admin.register(ProjectsModel)
class ProjectsAdmin(admin.ModelAdmin):
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


@admin.register(GetHelpModel)
class GetHelpModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone'
        )
    
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    search_fields = ['first_name', 'last_name', 'email', 'phone']


@admin.register(VolunteerMoodel)
class VolunteerMoodelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone'
        )
    
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

