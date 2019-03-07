from django.conf.urls import url 
from django.urls import path, include
from portal import views 
urlpatterns = [ 
     url(r'^$', views.HomePageView.as_view()),
     path('login/', views.login.as_view(),name='log_in'), 
     path('registration/', views.reg.as_view(),name='reg'), 
 ] 

