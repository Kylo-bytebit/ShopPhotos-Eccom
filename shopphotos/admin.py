from django.contrib import admin
from .models import ShopPhotos

class ShopPhotosAdmin(admin.ModelAdmin):
    list_display =('name', 'price', 'stock' )
    
admin.site.register(ShopPhotos, ShopPhotosAdmin)
 