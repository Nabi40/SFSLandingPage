from django.contrib import admin
from .models import aboutUss, SlideImage, MissionVision, Value, ExecutiveTeam

class SlideImageInline(admin.TabularInline):  # Allows adding images in aboutUss admin
    model = SlideImage
    extra = 1  # Allows adding one extra image


class MissionVisionInline(admin.StackedInline):  # Allows adding mission and vision
    model = MissionVision
    extra = 1


class ValueInline(admin.StackedInline):  # Allows adding values
    model = Value
    extra = 1


class ExecutiveTeamInline(admin.StackedInline):  # Allows adding executive members
    model = ExecutiveTeam
    extra = 1


@admin.register(aboutUss)
class aboutUssAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_description')  # Display fields in the list view
    search_fields = ('about_description',)  # Enables search
    inlines = [SlideImageInline, MissionVisionInline, ValueInline, ExecutiveTeamInline]  # Inline related models

    def save_model(self, request, obj, form, change):
        """Handles creation (POST) and updating (PUT)."""
        obj.save()

    def delete_model(self, request, obj):
        """Handles deletion."""
        obj.delete()


@admin.register(SlideImage)
class SlideImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_uss', 'image')
    search_fields = ('about_uss__about_description',)


@admin.register(MissionVision)
class MissionVisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_uss', 'our_mission', 'our_vision')
    search_fields = ('our_mission', 'our_vision')


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_uss', 'title', 'description')
    search_fields = ('title',)


@admin.register(ExecutiveTeam)
class ExecutiveTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_uss', 'name', 'position')
    search_fields = ('name', 'position')
