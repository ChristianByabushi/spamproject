from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from django.contrib import admin
from .views import *
router = routers.DefaultRouter()

admin.site.site_title = 'SpamCollect Administration'
admin.site.site_header = 'SpamCollect Admin'
admin.site.index_title = 'Collect'


urlpatterns = [
    path('api/', include(router.urls)),
    path('', index_view, name='/'),
    path('contact/', index_view, name='/contact'),
    path('send-feedback/', contactView, name='send-feedback'),
    path('about/', index_view, name='/about'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('message/', spamsMessageView, name='message'),
    path('stat/', statistic_views, name='stat'),
    path('download_csv/', download_csv, name='download_csv'),
]
