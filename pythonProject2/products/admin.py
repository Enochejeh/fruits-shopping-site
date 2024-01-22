from django.contrib import admin
from .models import Product, Offer

class OfferAdmin(admin.ModelAdmin):
    list_display =("code", 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "price")


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)




