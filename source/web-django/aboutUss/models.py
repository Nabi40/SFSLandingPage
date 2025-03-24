from django.db import models
from django.utils.timezone import now

class aboutUss(models.Model):
    about_description = models.CharField(max_length=255, default="Default description statement")
    slide_image1 = models.ImageField(upload_to='slide_image1/', blank=True, null=True)
    slide_image2 = models.ImageField(upload_to='slide_image2/', blank=True, null=True)
    slide_image3 = models.ImageField(upload_to='slide_image3/', blank=True, null=True)
    our_mission = models.CharField(max_length=255, default="Default mission statement")
    our_vision = models.CharField(max_length=255, default="Default vision statement")

    we_values = models.CharField(max_length=50, default="Default statement")
    values_title1 = models.CharField(max_length=50, default="Default statement")
    values_description1 = models.CharField(max_length=255, default="Default statement")
    values_title2 = models.CharField(max_length=50, default="Default statement")
    values_description2 = models.CharField(max_length=255, default="Default statement")
    values_title3 = models.CharField(max_length=50, default="Default statement")
    values_description3 = models.CharField(max_length=255, default="Default statement")
    values_title4 = models.CharField(max_length=50, default="Default statement")
    values_description4 = models.CharField(max_length=255, default="Default statement")
    # created_at = models.DateTimeField(auto_now_add=True, default=now)
    # updated_at = models.DateTimeField(auto_now=True, default=now)


    def __str__(self):
        return self.title

