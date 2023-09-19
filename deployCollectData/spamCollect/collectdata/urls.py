
from django.contrib import admin
from django.urls import path, include 
from django.views.generic import TemplateView 
from django.contrib import admin

admin.site.site_title = 'SpamCollect Administration'
admin.site.site_header = 'SpamCollect Admin'
admin.site.index_title = 'Collect'

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('webapp.urls') ),  
    #  path('', TemplateView.as_view(template_name='index.html')),
] 
