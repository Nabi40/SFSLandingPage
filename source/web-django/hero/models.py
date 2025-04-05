from django.db import models

class hero(models.Model):  # Kept "hero" as per your preference
    hero_title = models.CharField(max_length=255, default="Default description statement")
    hero_description = models.CharField(max_length=255, default="Default description statement")

    def __str__(self):
        return f"{self.hero_title} - {self.hero_description}"

class SlideImage(models.Model):
    hero_title = models.ForeignKey(hero, related_name="slide_images", on_delete=models.CASCADE)
    slide_image = models.ImageField(upload_to="slide_images/")

    def __str__(self):
        return self.slide_image.url if self.slide_image else "No Image"
    

class SlideLogos(models.Model):
    hero_title = models.ForeignKey(hero, related_name="slide_logos", on_delete=models.CASCADE)
    slide_logo = models.ImageField(upload_to="slide_logos/")

    def __str__(self):
        return self.slide_logo.url if self.slide_logo else "No logo"   
    

class StableLogos(models.Model):
    hero_title = models.ForeignKey(hero, related_name="stable_logos", on_delete=models.CASCADE)
    stable_logo = models.ImageField(upload_to="stable_logos/")
    sort_title = models.CharField(max_length=10, default="Default statement")
    sort_description = models.CharField(max_length=10, default="Default statement")

    def __str__(self):
        return f"{self.stable_logo} - {self.sort_title} - {self.sort_description}"


class OurService(models.Model):
    hero_title = models.ForeignKey(hero, related_name="service_logos", on_delete=models.CASCADE)
    ourservice_description = models.CharField(max_length=255, default="Default statement")

    service_logo = models.ImageField(upload_to="service_logo/")
    title = models.CharField(max_length=50, default="Default statement")
    description = models.CharField(max_length=255, default="Default statement")

    def __str__(self):
        return f"{self.ourservice_description} - {self.service_logo} - {self.title} - {self.description}"

class WorkDescription(models.Model):
    hero_title = models.ForeignKey(hero, related_name="work_description", on_delete=models.CASCADE)
    work_description = models.CharField(max_length=255, default="Default statement")

    work_logo = models.ImageField(upload_to="work_description/")
    title = models.CharField(max_length=50, default="Default statement")
    description = models.CharField(max_length=255, default="Default statement")

    def __str__(self):
        return f"{self.work_description} - {self.work_logo} - {self.title} - {self.description}"


class CustomerReview(models.Model):
    hero_title = models.ForeignKey(hero, related_name="name", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="name")

    customer_images = models.ImageField(upload_to="customer_image/")
    description = models.CharField(max_length=255, default="Default statement")
    rating = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])  # 1 to 5 stars


    def __str__(self):
        return f"{self.name} - {self.customer_images} - {self.description} - {self.rating}★"


class FAQ(models.Model):
    hero_title = models.ForeignKey(hero, related_name="question", on_delete=models.CASCADE)
    question = models.CharField(max_length=255, default="question question")
    answer = models.CharField(max_length=255, default="Default answer")

    def __str__(self):
        return f"{self.question} - {self.answer}"






