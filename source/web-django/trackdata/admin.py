from django.contrib import admin
from .models import SiteVisitReferences, ReferenceVisitLogs

class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in SiteVisitReferences._meta.fields]
    list_display = [field.name for field in SiteVisitReferences._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class ReadOnlyLogAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in ReferenceVisitLogs._meta.fields]
    list_display = [field.name for field in ReferenceVisitLogs._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(SiteVisitReferences, ReadOnlyAdmin)
admin.site.register(ReferenceVisitLogs, ReadOnlyLogAdmin)
