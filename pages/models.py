from django.db import models


class Banner(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class BannerPhotos(models.Model):
    photo = models.ImageField(upload_to = 'Banners/%Y/%m/%d/', blank = True)
    banner = models.ForeignKey(Banner, on_delete = models.DO_NOTHING, related_name='banner_photos')

class Contact(models.Model):
    company_logo = models.ImageField(upload_to = 'company_logo/', blank = True)
    country_code = models.CharField(max_length=3)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    facebook = models.URLField(max_length=255, blank=True)
    twitter = models.URLField(max_length=255, blank=True)
    youtube = models.URLField(max_length=255, blank=True)

class Subscriber(models.Model):
    subscriber_email = models.EmailField(max_length = 200)

    def __str__(self):
        return str(self.subscriber_email)