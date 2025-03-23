from django.db import models

class hero(models.Model):
    cover_image = models.ImageField(upload_to='cover_image/', blank=True, null=True)
    tab_image = models.ImageField(upload_to='tab_image/', blank=True, null=True)
    tab_title = models.CharField(max_length=255)
    tab_description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

