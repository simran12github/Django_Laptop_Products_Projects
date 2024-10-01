from django.db import models

# Create your models here.
class Laptop(models.Model):
    """
    we try to create a table for laptop with corresponding fields
    """
    brand_name = models.CharField(max_length=300)
    configurations = models.TextField(null=True)
    price = models.IntegerField(null=True)
    rating = models.FloatField(null=True)

    def __str__(self):
        return self.brand_name


class LapImage(models.Model):
    """
    if we create image field in Laptop model we can store one record only one image
    but we have stroe one record laptop should have more than one images for that we
    are creating this model so that one laptop record we can connect with n number images
    """
    image = models.FileField(upload_to="Laptop_images", null=True)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=50)

    def __str__(self):
        return self.image_name