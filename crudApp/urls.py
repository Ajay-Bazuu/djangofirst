from django.urls import path
from .views import *
urlpatterns = [
    path("",home, name='home'),
    path("form/",form, name='form'),
    path("contact/",contactus, name='contactus'),
    path("about/",aboutus, name='aboutus'),

]


