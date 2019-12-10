from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^aboutus$', views.aboutus,name='aboutus'),
    url(r'^enquiry$', views.aboutus, name='aboutus'),
]