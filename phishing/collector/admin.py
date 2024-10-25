from django.contrib import admin
from .models import Target,User

class TargetAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","count","is_completed"]
    list_filter = ["is_completed","count"]
    def first_name(slef,Target):
        return Target.user.first_name
    
    def last_name(slef,Target):
        return Target.user.last_name

admin.site.register(Target,TargetAdmin)
