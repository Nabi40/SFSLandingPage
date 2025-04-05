from django.db import models

class aboutUss(models.Model):  # Kept "aboutUss" as per your preference
    about_description = models.CharField(max_length=255, default="Default description statement")

    def __str__(self):
        return self.about_description


class SlideImage(models.Model):
    about_uss = models.ForeignKey(aboutUss, related_name="slide_images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="slide_images/")

    def __str__(self):
        return self.image.url if self.image else "No Image"


class MissionVision(models.Model):
    about_uss = models.ForeignKey(aboutUss, related_name="mission", on_delete=models.CASCADE)
    our_mission = models.CharField(max_length=255, default="Default mission statement")
    our_vision = models.CharField(max_length=255, default="Default vision statement")

    def __str__(self):
        return f"{self.our_mission} | {self.our_vision}"

class Value(models.Model):
    about_uss = models.ForeignKey(aboutUss, related_name="values", on_delete=models.CASCADE)
    value_description = models.CharField(max_length=255, default="Default statement")

    title = models.CharField(max_length=50, default="Default statement")
    description = models.CharField(max_length=255, default="Default statement")

    def __str__(self):
        return self.title


class ExecutiveTeam(models.Model):
    about_uss = models.ForeignKey(aboutUss, related_name="executive_team", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default="description description ")
    profile_image = models.ImageField(upload_to="profile_images/")

    def __str__(self):
        return f"{self.name} - {self.position} - {self.description} - {self.profile_image}"
