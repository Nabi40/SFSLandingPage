from django.db import models
import string
import random

def generate_random_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=16))

class Reference(models.Model):
    id = models.CharField(primary_key=True, max_length=16, default=generate_random_id, editable=False, unique=True)
    source = models.CharField(max_length=255, blank=False)
    specifics = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.source}"


class AnotherModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
