from django.contrib import admin
from .models import hero, SlideImage, SlideLogos, StableLogos, OurService, WorkDescription, CustomerReview, FAQ

@admin.register(hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("id", "hero_title", "hero_description")  # Only using id until you confirm field names

@admin.register(SlideImage)
class SlideImageAdmin(admin.ModelAdmin):
    list_display = ("id", "slide_image")

@admin.register(SlideLogos)
class SlideLogosAdmin(admin.ModelAdmin):
    list_display = ("id", "slide_logo")

@admin.register(StableLogos)
class StableLogosAdmin(admin.ModelAdmin):
    list_display = ("id", "hero_title", "sort_title", "sort_description")

@admin.register(OurService)
class OurServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")

@admin.register(WorkDescription)
class WorkDescriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "work_description", "work_logo", "title", "description")  

@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ("id","name", "customer_images", "description", "rating")

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "answer")
