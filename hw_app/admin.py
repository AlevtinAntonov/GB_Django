from django.contrib import admin
from .models import Customer, Product, Order, CategoryProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'count', 'image']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'registered_at']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(CategoryProduct)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
