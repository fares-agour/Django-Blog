from django.contrib import admin
from django.urls import path
from . import views
app_name = 'contact'
urlpatterns = [
    path("",views.contact, name='contact'),
    # path("success/",views.success, name='success'),

]
