from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    order_by = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Listing(models.Model):

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    listing_name = models.CharField(max_length=250, null=True)
    price = models.CharField(max_length=250, null=True)
    short_description = models.CharField(max_length=720)
    description = models.TextField()
    bedroom = models.CharField(max_length=250, null=True, blank=True,)
    bathroom = models.CharField(max_length=250, null=True, blank=True,)
    lease = models.CharField(max_length=250, null=True, blank=True)
    contact_name = models.CharField(max_length=250, null=True)
    email_address = models.CharField(max_length=250, null=True)
    contact_number = models.CharField(max_length=12, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_one = models.ImageField(null=True, blank=True)
    image_two = models.ImageField(null=True, blank=True)
    image_three = models.ImageField(null=True, blank=True)
    image_four = models.ImageField(null=True, blank=True)
    image_five = models.ImageField(null=True, blank=True)
    image_six = models.ImageField(null=True, blank=True)
    image_seven = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.listing_name
