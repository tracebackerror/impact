"""spritual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from models import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('models.urls')),
    path('',views.index, name="home"),
    path('about/',views.about,name='about'),
    path('blog_details/<int:blog_id>/', views.blog_details, name='blog_details'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('donation_details/',views.donation_details,name='donation_details'),
    path('donation_listing/',views.donation_listing,name='donation_listing'),
    path('event_details/<int:event_id>/',views.event_details,name='event_details'),
    path('events/',views.events,name='events'),
    path('faq/',views.faq,name='faq'),
    path('product_details/',views.product_details,name='product_details'),
    path('products/',views.products,name='products'),
    path('service/',views.service,name='service'),
    path('stories_details/',views.stories_details,name='stories_details'),
    path('stories/',views.stories,name='stories'),
    path('volunteers/',views.volunteers,name='volunteers'),
]
