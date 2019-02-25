#encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#发布会表
class Photo(models.Model):
    photo_url=models.CharField(max_length=100) #相片url
    car_name=models.CharField(max_length=100) #车系名字
    car_groupId=models.IntegerField() #车系id
    isPass=models.IntegerField() #是否通过
    deviceType=models.IntegerField() #设备类型1.iphone2.android
    buildId=models.CharField(max_length=100) #版本
    create_time=models.DateField(auto_now=True) #创建时间

    def __unicode__(self):
        return self.car_name