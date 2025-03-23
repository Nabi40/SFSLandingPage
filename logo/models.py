from django.db import models

class logo(models.Model):
    client_image = models.ImageField(upload_to='client_image/', blank=True, null=True)
    logo_image = models.ImageField(upload_to='logo_image/', blank=True, null=True)
    logo_title = models.CharField(max_length=255)
    logo_description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

