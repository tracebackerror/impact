from django.contrib import admin
from .models import *
import base64
from django.utils.html import format_html


@admin.register(EventModel)
class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    search_fields = ['title_name', ]
    
    list_display = ('id', 'title_name', 'event_date', 'created_date','modified_date')
    
    readonly_fields = ["thumbnail_497_x_499",
                       "view_event_detailed_pagephoto",
                       "view_event_banner_pagephoto"
                       ]
    def thumbnail_497_x_499(self, obj):
        return format_html('<img src="{}">', obj.photo)
    def view_event_detailed_pagephoto(self, obj):
        return format_html('<img src="{}">', obj.event_detailed_pagephoto)
    
    def view_event_banner_pagephoto(self, obj):
        return format_html('<img src="{}">', obj.event_banner_pagephoto)
    
    
@admin.register(ContactModel)
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

