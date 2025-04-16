import string
import random
from django.db import models

def generate_random_id(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class SiteVisitReferences(models.Model):
    id = models.CharField(primary_key=True, max_length=16, default=generate_random_id, editable=False)
    source = models.CharField(max_length=255)
    specifics = models.TextField(blank=True)

    def __str__(self):
        return f"{self.source} - {self.id}"

class ReferenceVisitLogs(models.Model):
    visit_date = models.DateTimeField(auto_now_add=True)
    visit_ref = models.ForeignKey(SiteVisitReferences, on_delete=models.CASCADE, related_name='visits')

    def __str__(self):
        return f"Visit on {self.visit_date} from {self.visit_ref.id}"
