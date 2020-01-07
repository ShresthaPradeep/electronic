from django.contrib import admin
from .models import Category, Brand, Type, Feature, Product, SubImage, Color, Specification

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Feature)

class ColorTabularInline(admin.TabularInline):
    model = Color

class SubImageTabularInline(admin.TabularInline):
    model = SubImage

class SpecificationTabularInline(admin.TabularInline):
    model = Specification

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        SubImageTabularInline,
        ColorTabularInline,
        SpecificationTabularInline,
    ]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

admin.site.register(Color)
admin.site.register(SubImage)
admin.site.register(Specification)