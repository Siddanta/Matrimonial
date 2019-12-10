from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import login, settings
from django.contrib.auth import views as auth_views

from .views import profile_detail

app_name = 'accounts'

urlpatterns = [

    #url('^login/$', views.login),
    url('^login/$', login,{'template_name' : 'accounts/login.html'}),

    # url(r'^register/$', CreateArtistView.as_view(), name='register'),
    url(r'^register/$', views.register, name='register'),
    url(r'^search/',views.search,name='search'),
    #url(r'^create/$', views.register, name='register'),
    #url(r'^(?P<pk>\w+)/$', ProfileDetailView.as_view()),
    url(r'^profile/',profile_detail),

    #url(r'^(?P<slug>[\w.@+-]+)/edit/$', views.edit_prof, name='edit'),

    #url(r'^<int:id>$', ProfileDetailView.as_view(), name='profile')
    url(r'^register1/$', views.register1, name='register1'),
    url(r'^register2/$', views.register2, name='register2'),
    url(r'^register3/$', views.register3, name='register3'),
    url(r'^register4/$', views.register4, name='register4'),
    url(r'^register5/$', views.register5, name='register5'),
    url(r'^register6/$', views.register6, name='register6'),
    url(r'^afterLogin/$', views.after_login, name='after_login'),
    #path('<int:my_username>/', views.profile_details, name='detail'),
    path('details/<str:my_username>/', views.profile_details, name='detail'),

    path('edit_all', views.edit_prof, name='edit'),
    path('edit_username',views.edit_username,name='edit_username'),
    path('password',views.edit_password,name='edit_password'),
    path('password',views.edit_password,name='edit_password'),
    path('<int:my_id>/my_record',views.edit_register1, name='edit_register1'),
    path('<int:my_id>/my_record/1',views.edit_register2, name='edit_register2'),
    path('<int:my_id>/my_record/2',views.edit_register3, name='edit_register3'),
    path('<int:my_id>/my_record/3',views.edit_register4, name='edit_register4'),
    path('<int:my_id>/my_record/4',views.edit_register5, name='edit_register5'),
    path('<int:my_id>/my_record/5',views.edit_register6, name='edit_register6'),

    # path('password',views.edit_password,name='edit_password'),
    # path('password',views.edit_password,name='edit_password'),




    url(r'^logout/$', auth_views.logout, name='logout'),

    #url(r'^add/user/$', views.userview, name='userview'),
]