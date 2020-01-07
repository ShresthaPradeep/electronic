from django.db import models



class Brand(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to = 'brands/', blank = True)
    photo = models.ImageField(upload_to = 'brands/', blank = True)
    
    def __str__(self):
        return self.name
    
class Type(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to = 'types/', blank = True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Feature(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to = 'feature_products/', blank = True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    feature = models.ForeignKey(Feature, blank = True, null = True, on_delete=models.DO_NOTHING, related_name='feature_products')
    brand = models.ForeignKey(Brand, blank = True, null = True, on_delete=models.DO_NOTHING, related_name='brand_products')
    category = models.ForeignKey(Category, blank = True, null = True, on_delete=models.DO_NOTHING, related_name='category_products')
    product_type = models.ForeignKey(Type, blank = True, null = True, on_delete=models.DO_NOTHING, related_name='type_products')
    available = models.BooleanField(default=True, null=True, blank=True)
    marked_price = models.IntegerField(blank=True, null=True)
    selling_price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True, unique=True)
    photo_main = models.ImageField(upload_to = 'products/%Y/%m/%d/')
    thumbnail_main = models.ImageField(upload_to = 'products/thumbnails/%Y/%m/%d/')

    def __str__(self):
        return self.name


class SubImage(models.Model):
    product = models.ForeignKey(Product, blank = True, null = True, on_delete=models.DO_NOTHING, related_name='product_image')
    sub_image = models.ImageField(upload_to = 'products/%Y/%m/%d/', blank = True)
    sub_thumbnail = models.ImageField(upload_to = 'products/thumbnails/%Y/%m/%d/', blank = True)

class Color(models.Model):
    product = models.ForeignKey(Product, blank = True, null = True, on_delete=models.DO_NOTHING, related_name='product_color' )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Specification(models.Model):
    product = models.ForeignKey(Product, blank = True, null = True, on_delete=models.DO_NOTHING, related_name='product_spec' )
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)