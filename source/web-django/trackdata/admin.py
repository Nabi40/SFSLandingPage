from django.contrib import admin
from .models import Reference, AnotherModel

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('count', 'id', 'source', 'specifics', 'created_at', 'updated_at')
    search_fields = ('id', 'source', 'specifics')
    readonly_fields = ('id', 'source', 'specifics', 'created_at', 'updated_at')

    def count(self, obj):
        return Reference.objects.filter(created_at__lte=obj.created_at).count()
    count.short_description = 'Entry No.'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(AnotherModel)
class AnotherModelAdmin(admin.ModelAdmin):
    list_display = ('count', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('name', 'created_at', 'updated_at')

    def count(self, obj):
        return AnotherModel.objects.filter(created_at__lte=obj.created_at).count()
    count.short_description = 'Entry No.'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True
