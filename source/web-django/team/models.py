from django.db import models

class OurTeam(models.Model): 
    description = models.CharField(max_length=255, default="Default description statement")
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.description} - {self.image}"


class Head(models.Model):
    description = models.CharField(max_length=255, default="Default description statement")

    def __str__(self):
        return self.description

class HeadTeam(models.Model):
    head = models.ForeignKey(Head, related_name="head", on_delete=models.CASCADE) 
    image = models.ImageField(upload_to="slide_images/")
    name = models.CharField(max_length=150, default="Default statement")
    designation = models.CharField(max_length=100, default="executive executive executive")


    def __str__(self):
        return f"{self.image} - {self.name} - {self.designation}"
    

class AllTeamDescrip(models.Model):
    description = models.CharField(max_length=255, default="Default description statement")

    def __str__(self):
        return self.description

class AllTeam(models.Model):
    allteam = models.ForeignKey(AllTeamDescrip, related_name="Allteam", on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="profile_images/")

    def __str__(self):
        return f"{self.name} - {self.position} - {self.profile_image}"
