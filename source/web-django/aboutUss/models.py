from django.db import models

class SlideImage(models.Model):
    image = models.ImageField(upload_to="slide_images/", blank=True, null=True)

    def __str__(self):
        return self.image.url if self.image else "No Image"


class aboutUss(models.Model):
    about_description = models.CharField(max_length=255, default="Default description statement")

    def __str__(self):
        return self.about_description


class Mission_vision(models.Model):
    our_mission = models.CharField(max_length=255, default="Default mission statement")
    our_vision = models.CharField(max_length=255, default="Default vision statement")


class Value(models.Model):
    value_description = models.CharField(max_length=255, default="Default statement")
    title = models.CharField(max_length=50, default="Default statement")
    description = models.CharField(max_length=255, default="Default statement")
    


class ExecutiveTeam(models.Model):
    about_uss = models.ForeignKey(aboutUss, related_name="executive_team", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.position}"
