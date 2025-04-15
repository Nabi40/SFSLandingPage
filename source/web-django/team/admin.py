from django.contrib import admin
from .models import OurTeam, Head, HeadTeam, AllTeamDescrip, AllTeam


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'image')


@admin.register(Head)
class HeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(HeadTeam)
class HeadTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'head', 'name', 'designation', 'image')
    list_filter = ('designation',)
    search_fields = ('name', 'designation')


@admin.register(AllTeamDescrip)
class AllTeamDescripAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(AllTeam)
class AllTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'allteam', 'name', 'position', 'profile_image')
    list_filter = ('position',)
    search_fields = ('name', 'position')

    
