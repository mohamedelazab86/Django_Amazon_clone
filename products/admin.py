from django.contrib import admin
from .models import Product,Brand,Review,ImageProduct



# customize   product
class Imgeadmininline(admin.TabularInline):
    model=ImageProduct
class Productadmin(admin.ModelAdmin):
    list_display=['name','sku','flag']
    list_filter=['price']
    search_fields=['name','price']
    inlines=[Imgeadmininline]


# Register your models here.
admin.site.register(Product,Productadmin)
admin.site.register(Brand)
admin.site.register(Review)

