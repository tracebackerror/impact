from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [ 
    # path('',views.index, ),
    path('', views.indexview.as_view(),name='index'),
    path('about/', views.aboutview.as_view(),name='about'),
    path('blog_details/', views.blog_details_view.as_view(),name='blog_details'),
    path('blog/', views.blogview.as_view(),name='blog'),
    path('contact/', views.contactview.as_view(),name='contact'),
    path('donation_details/', views.donation_details_view.as_view(),name='donation_details'),
    path('donation_listing/', views.donation_listing_view.as_view(),name='donation_listing'),
    path('event_details/', views.event_details_view.as_view(),name='event_details'),
    path('events/', views.eventsview.as_view(),name='events'),
    path('faq/', views.faqview.as_view(),name='faq'),
    path('product_details/', views.product_details_view.as_view(),name='product_details'),
    path('products/', views.productsview.as_view(),name='products'),
    path('service/', views.serviceview.as_view(),name='service'),
    path('stories_details/', views.stories_details_view.as_view(),name='stories_details'),
    path('stories/', views.storiesview.as_view(),name='stories'),
    path('volunteers/', views.volunteersview.as_view(),name='volunteers'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)