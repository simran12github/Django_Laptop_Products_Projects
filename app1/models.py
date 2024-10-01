from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    desc = models.TextField()
    rating = models.FloatField()
    created = models.DateField(auto_now=True)
    org_email = models.EmailField()
    org_website = models.URLField()
    pro_image = models.FileField(upload_to="product_images")

    def __str__(self):
        return self.name

    def offer(self):
        return self.price - 3000

    @property
    def custrate(self):
        return self.rating-1

    def save(self, *args, **kwargs):
        self.price = self.price+2000
        super(Product,self).save(*args, **kwargs)

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name

class Profile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.person.last_name


"""
groupby, fetching data, filter, condition, logical, comparison, like,aggregate, annotate, not in, in...etc
alter table, create, drop
"""