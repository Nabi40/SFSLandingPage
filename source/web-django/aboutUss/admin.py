from django.contrib import admin
from .models import aboutUss, SlideImage, MissionVision, Value, ExecutiveTeam


class SlideImageInline(admin.TabularInline):
    model = SlideImage
    extra = 1
    show_change_link = True  # Allows editing from inline


class MissionVisionInline(admin.StackedInline):
    model = MissionVision
    extra = 1
    show_change_link = True


class ValueInline(admin.StackedInline):
    model = Value
    extra = 1
    show_change_link = True


class ExecutiveTeamInline(admin.StackedInline):
    model = ExecutiveTeam
    extra = 1
    show_change_link = True


@admin.register(aboutUss)
class aboutUssAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_description')
    search_fields = ('about_description',)
    inlines = [SlideImageInline, MissionVisionInline, ValueInline, ExecutiveTeamInline]

    # Optional: Add readonly fields or custom admin form handling
    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
        obj.delete()


@admin.register(SlideImage)
class SlideImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_uss', 'image')
    search_fields = ('about_uss__about_description',)
    list_filter = ('about_uss',)


@admin.register(MissionVision)
class MissionVisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_uss', 'our_mission', 'our_vision')
    search_fields = ('our_mission', 'our_vision')
    list_filter = ('about_uss',)


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_uss', 'title', 'description')
    search_fields = ('title',)
    list_filter = ('about_uss',)


@admin.register(ExecutiveTeam)
class ExecutiveTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_uss', 'name', 'position', 'description', 'profile_image')
    search_fields = ('name', 'position', 'description')
    list_filter = ('about_uss',)
