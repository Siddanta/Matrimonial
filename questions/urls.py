from django.urls import path
from . import views


urlpatterns = [

    path('home',views.home, name='home'),
    path('match_all',views.match_all, name ='match_all'),
    path('<int:id>',views.single, name='question_single'),

]