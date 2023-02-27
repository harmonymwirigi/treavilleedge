from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name='index'),
    path('counter',views.counter,name='counter'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('create',views.create,name='create'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('404',views.Error_404,name='Error_404'),
    path('clientsignup',views.clientsignup,name='clientsignup'),
    path('helpandfaqs',views.helpandfaqs,name='helpandfaqs'),
    path('howitworks',views.howitworks,name='howitworks'),
    path('reusecode',views.reusecode,name='reusecode'),
    path('services',views.services,name='services'),
    path('transporter',views.transporter,name='transporter'),
    path('transporterdashboard',views.transporterdashboard,name='transporterdashboard'),




    path('post/<str:pk>',views.post,name='post')
]