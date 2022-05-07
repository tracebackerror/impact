from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id',
    'first_name', 'last_name', 'email','phone','comments','created_date','modified_date')


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


admin.site.register(GetHelpModel)
admin.site.register(VolunteerMoodel)
admin.site.register(SiteInfoModel)
