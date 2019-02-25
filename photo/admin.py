from django.contrib import admin
from photo.models import Photo
class PhotoAdmin(admin.ModelAdmin):
    list_display=['photo_url','car_name','car_groupId','isPass','deviceType','buildId','create_time']
    search_fields=['car_name','car_groupId','photo_url']
    list_filter=['isPass','deviceType','buildId']

# Register your models here.
admin.site.register(Photo,PhotoAdmin)
