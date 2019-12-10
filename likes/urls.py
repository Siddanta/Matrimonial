from django.urls import path

from . import views
app_name = 'likes'
urlpatterns = [
    path('<int:id>/',views.like_user,name='like_user')
    #url(r'^$', views.like_user, name='like_user'),
]
