from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id',
    'first_name', 'last_name', 'email','phone','comments','created_date','modified_date')


admin.site.register(ProjectsModel)
admin.site.register(StoriesModel)
admin.site.register(GetHelpModel)
admin.site.register(VolunteerMoodel)
