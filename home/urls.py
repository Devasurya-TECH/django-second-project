from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contacts', views.contacts),
    path('booking', views.booking),
    path('doctors', views.doctors),
    path('services',views.services),
]

