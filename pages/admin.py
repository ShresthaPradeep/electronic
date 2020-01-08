from django.contrib import admin
from .models import Banner, BannerPhotos, Contact, Subscriber

class BannerTabularInline(admin.TabularInline):
    model = BannerPhotos

class BannerAdmin(admin.ModelAdmin):
    inlines = [BannerTabularInline]
    class Meta:
        model = Banner


admin.site.register(Banner, BannerAdmin)
admin.site.register(BannerPhotos)

admin.site.register(Contact)
admin.site.register(Subscriber)