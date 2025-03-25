from django.contrib import admin
from .models import aboutUss, SlideImage, MissionVision, Value, ExecutiveTeam

class aboutUssAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_description')  # Fields to display in the list view
    search_fields = ['about_description']  # Enable search by description
    list_filter = ['about_description']  # Add a filter option in the list view

class SlideImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_uss', 'image')  # Fields to display
    list_filter = ['about_uss']  # Filter by the aboutUss foreign key

# Register the custom admin classes
admin.site.register(aboutUss, aboutUssAdmin)
admin.site.register(SlideImage, SlideImageAdmin)
admin.site.register(MissionVision)
admin.site.register(Value)
admin.site.register(ExecutiveTeam)
