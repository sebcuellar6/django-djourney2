from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=35, default='Unknown City')
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    image_url = models.TextField()

    def __str__(self):
        return self.name

class Attraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attraction')
    name = models.CharField(max_length=35, default='Unknown Attraction')
    demographic = models.CharField(max_length=150)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Review(models.Model):
    reviewer_name = models.CharField(max_length=25)
    stars = models.CharField(max_length=2)
    description = models.CharField(max_length=125)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='review')

    def __str__(self):
        return self.reviewer_name