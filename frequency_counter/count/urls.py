from django.contrib import admin
from django.urls import path
from . import views
  
urlpatterns = [
    path('frequency/', views.frequency_form,name='frequency_form' ),
    path('result/',views.count_word,name='count_word'),
]
