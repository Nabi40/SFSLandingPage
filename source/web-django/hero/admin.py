from django.contrib import admin
from .models import (hero, SlideImage, Logos, OurService,
                      WorkDescription, CustomerReview, 
                      FAQ, SlideLogo, Service, Office, 
                      Inquiry, Subscribe)

class SlideImageInline(admin.TabularInline):
    model = SlideImage
    extra = 1

@admin.register(hero)
class heroAdmin(admin.ModelAdmin):
    list_display = ('id', 'hero_title', 'hero_description')
    search_fields = ('hero_title', 'hero_description')
    inlines = [SlideImageInline]

@admin.register(SlideImage)
class SlideImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'hero', 'image')
    search_fields = ('hero__hero_title',)


@admin.register(Logos)
class LogosAdmin(admin.ModelAdmin):
    list_display = ('id', 'stable_logo', 'sort_title', 'sort_description')
    search_fields = ('sort_title', 'sort_description')


@admin.register(SlideLogo)
class SlideLogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'slide_logo')
    search_fields = ('logos__sort_title',)

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

@admin.register(OurService)
class OurServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'ourservice_description')
    inlines = [ServiceInline]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')

@admin.register(WorkDescription)
class WorkDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')

@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rating')
    search_fields = ('name', 'description')
    list_filter = ('rating',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')
    search_fields = ('question', 'answer')


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'company_name', 'email', 'phone_number', 'message')
    search_fields = ('full_name', 'company_name', 'email', 'phone_number', 'message')


@admin.register(Office)
class OfficAedmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'email', 'phone_number')
    search_fields = ('address', 'email', 'phone_number')


@admin.register(Subscribe)
class SubscribeAedmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('email',)