from django.contrib import admin
from . models import ContactForm

# Register your models here.
@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','comments','created_date','modified_date')