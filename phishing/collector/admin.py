from django.contrib import admin
from .models import Target

class ModelAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name')

admin.site.register(Target,ModelAdmin)
