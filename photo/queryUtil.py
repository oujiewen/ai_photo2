#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from models import Photo

def queryPhotoAdmin(request):
    if request.method=='GET':
        querySet=Photo.objects.all()
        return render(request,'listptoto.html',{'photos':querySet})
    else:
        filter=makeFilter(request)
        print filter
        querySet=Photo.objects.filter(**filter)
        return render(request,'listptoto.html',{'photos':querySet,'filter':filter})


def checkParmes(request,list):
    parmes=request.POST
    print parmes
    for key in parmes:
        if key not in list:
            return HttpResponse('传参错误')
            break

def makeFilter(request):
    filter={}
    query_id=request.POST.get('id')     #从requset获取查询的值
    query_car_name = request.POST.get('car_name')
    query_photo_url = request.POST.get('photo_url')
    query_car_groupId = request.POST.get('car_groupId')
    query_car_isPass = request.POST.get('isPass')
    query_deviceType = request.POST.get('deviceType')
    query_buildId=request.POST.get('buildId')
    query_create_time_begin=request.POST.get('create_time_begin')
    query_create_time_end=request.POST.get('create_time_end')
    if query_id:
        filter['id'] = query_id
    if query_car_name:
        filter['car_name'] = query_car_name
    if query_photo_url:
        filter['photo_url'] = query_photo_url
    if query_car_groupId:
        filter['car_groupId'] = query_car_groupId
    if query_car_isPass:
        filter['isPass'] = query_car_isPass
    if query_deviceType:
        filter['deviceType'] = query_deviceType
    if query_buildId:
        filter['buildId'] = query_buildId
    if query_create_time_begin and query_create_time_end:
        list=[query_create_time_begin,query_create_time_end]
        filter['create_time__range'] = list
    else:
        if query_create_time_begin:
            filter['create_time__gte'] = query_create_time_begin
        if  query_create_time_end:
            filter['create_time__lte'] = query_create_time_end
    return filter

def deletePhoto(requset,id):
    Photo.objects.filter(id=id).delete()
    return HttpResponseRedirect("/photo/queryAdmin/")

def getPhoto(requset,id):
    photo=Photo.objects.filter(id=id)
    print photo
    return render(requset,'updatePhoto.html',{'photos':photo})

def addPhoto(requset):
    return render(requset,'updatePhoto.html')

def updatePhoto(requset,id):
    query_car_id = requset.POST.get('id')
    query_car_name = requset.POST.get('car_name')
    query_photo_url = requset.POST.get('photo_url')
    query_car_groupId = requset.POST.get('car_groupId')
    query_car_isPass = requset.POST.get('isPass')
    query_deviceType = requset.POST.get('deviceType')
    query_buildId=requset.POST.get('buildId')
    print id
    if id=='0':
        Photo.objects.create(car_name=query_car_name,photo_url=query_photo_url,car_groupId=query_car_groupId,
                                      isPass=query_car_isPass,deviceType=query_deviceType,buildId=query_buildId)
        print 'add'
    else:
        Photo.objects.filter(id=id).update(car_name=query_car_name,photo_url=query_photo_url,car_groupId=query_car_groupId,
                                      isPass=query_car_isPass,deviceType=query_deviceType,buildId=query_buildId)
        print 'update'
    return HttpResponseRedirect("/photo/queryAdmin/")





