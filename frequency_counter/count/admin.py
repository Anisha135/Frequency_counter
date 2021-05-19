from django.contrib import admin
from .models import frequency_model,count_model

admin.site.register(frequency_model)
admin.site.register(count_model)