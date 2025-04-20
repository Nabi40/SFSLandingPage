from django.db import models

class hero(models.Model):
    hero_title = models.CharField(max_length=255, default="Default description statement")
    hero_description = models.CharField(max_length=400, default="Default description statement")
    image_mobile = models.ImageField(upload_to="image_mobile/", default='default_image.jpg')
    image_lgMobile = models.ImageField(upload_to="image_lgMobile/", default='default_image.jpg')
    image_desktop = models.ImageField(upload_to="image_desktop/", default='default_image.jpg')
    button_link = models.CharField(max_length=255, default="http//###########")
    button = models.CharField(max_length=255, default="JOIN US")

    def __str__(self):
        return f" {self.hero_title} - {self.hero_description} - {self.image_mobile.url} - {self.image_lgMobile.url} - {self.image_desktop.url}"
    

class Logos(models.Model):
    stable_logo = models.ImageField(upload_to="stable_logos/")
    sort_title = models.CharField(max_length=50, default="Default statement")
    sort_description = models.CharField(max_length=100, default="Default statement")

    def __str__(self):
        return f"{self.stable_logo.url if self.stable_logo else 'No Image'} - {self.sort_title} - {self.sort_description}"


class SlideLogo(models.Model):
    slide_logo = models.ImageField(upload_to="slide_logos/")

    def __str__(self):
        return f"{self.slide_logo.url if self.slide_logo else 'No Image'}"
    

class OurService(models.Model):
    ourservice_description = models.CharField(max_length=400, default="Default statement")

    def __str__(self):
        return f"{self.ourservice_description}"
    
class Service(models.Model):
    service_detail = models.ForeignKey(OurService, related_name="service", on_delete=models.CASCADE)
    service_logo = models.ImageField(upload_to="service_logo/")
    title = models.CharField(max_length=50, default="Default statement")
    description = models.CharField(max_length=400, default="Default statement")
    
    def __str__(self):
        return f"{self.service_logo.url} - {self.title} - {self.description}"


class WorkDescriptionGroup(models.Model):
    work_description = models.CharField(max_length=400, default="Default statement")

    def __str__(self):
        return self.work_description


class WorkDescription(models.Model):
    work_logo = models.ImageField(upload_to="work_description/")
    title = models.CharField(max_length=100, default="Default statement")
    description = models.CharField(max_length=400, default="Default statement")

    def __str__(self):
        return f"{self.work_logo} - {self.title} - {self.description}"



class CustomerReview(models.Model):
    name = models.CharField(max_length=400, default="customer_reviews")
    customer_images = models.ImageField(upload_to="customer_image/")
    description = models.CharField(max_length=400, default="Default statement")
    rating = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])  # 1 to 5 stars


    def __str__(self):
        return f"{self.name} - {self.customer_images.url} - {self.description} - {self.rating}★"


class FAQ(models.Model):
    question = models.CharField(max_length=400, default="question question")
    answer = models.CharField(max_length=400, default="Default answer")

    def __str__(self):
        return f"{self.question} - {self.answer}"


class Inquiry(models.Model):
    full_name = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    

class Office(models.Model):
    address = models.CharField(max_length=205)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)


class Subscribe(models.Model):
    email = models.EmailField()