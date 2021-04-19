
from django.contrib import admin
from .models import Listing, Category


class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'listing_name',
        'price',
        'short_description',
        'image',
        'date',
    )

    ordering = ('date',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'order_by',
    )

    ordering = ('order_by',)


admin.site.register(Listing, ListingAdmin)
admin.site.register(Category, CategoryAdmin)
