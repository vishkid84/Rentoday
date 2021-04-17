from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Listing(models.Model):

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    listing_name = models.CharField(max_length=250, null=True, blank=True,)
    price = models.CharField(max_length=250, null=True, blank=True,)
    short_description = models.CharField(max_length=720)
    description = models.TextField()
    bedroom = models.CharField(max_length=250, null=True, blank=True,)
    bathroom = models.CharField(max_length=250, null=True, blank=True,)
    lease = models.CharField(max_length=250)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.listing_name
