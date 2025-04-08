from django.contrib import admin
from .models import aboutUss, SlideImage, MissionVision, Value, ValueDetail, ExecutiveTeam


class SlideImageInline(admin.TabularInline):
    model = SlideImage
    extra = 1


@admin.register(aboutUss)
class AboutUssAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_description')
    inlines = [SlideImageInline]


@admin.register(MissionVision)
class MissionVisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'our_mission', 'our_vision')


class ValueDetailInline(admin.TabularInline):
    model = ValueDetail
    extra = 1


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'value_description')
    inlines = [ValueDetailInline]


@admin.register(ExecutiveTeam)
class ExecutiveTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'description', 'profile_image')


# SlideImage and ValueDetail are already managed inline, but you can still register them if needed
@admin.register(SlideImage)
class SlideImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_uss', 'image')


@admin.register(ValueDetail)
class ValueDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'Value', 'title', 'description')
