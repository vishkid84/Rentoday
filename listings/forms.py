from django import forms
from .models import Category, Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            'category',
            'listing_name',
            'price',
            'short_description',
            'description',
            'bedroom',
            'bathroom',
            'lease',
            'contact_name',
            'email_address',
            'contact_number',
            'image',
            'image_one',
            'image_two',
            'image_three',
            'image_four',
            'image_five',
            'image_six',
            'image_seven',
        ]
