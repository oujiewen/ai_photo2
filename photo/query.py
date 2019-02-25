#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from photo.models import Photo
from django.http import JsonResponse

def deal_query_set(result):  #处理查询set[]转化成一个list，并return
    list=[]
    for x in result:
        photo = {}
        photo['id'] = x.id
        photo['car_name'] = x.car_name
        photo['photo_url'] = x.photo_url
        photo['car_groupId'] = x.car_groupId
        photo['isPass'] = x.isPass
        photo['deviceType'] = x.deviceType
        photo['buildId'] = x.buildId
        photo['create_time'] = x.create_time
        list.append(photo)
    return list

def query_photo(request):
    parmes=request.POST
    list=['id','car_name','photo_url','car_groupId','isPass','deviceType','buildId','create_time_begin','create_time_end']
    print parmes
    for key in parmes:
        if key not in list:
            return JsonResponse({'STATUS': -1, 'message': '不合法字段1'+key}, json_dumps_params={'ensure_ascii': False})
            break
    query_id=request.POST.get('id')     #从requset获取查询的值
    query_car_name = request.POST.get('car_name')
    query_photo_url = request.POST.get('photo_url')
    query_car_groupId = request.POST.get('car_groupId')
    query_car_isPass = request.POST.get('isPass')
    query_deviceType = request.POST.get('deviceType')
    query_buildId=request.POST.get('buildId')
    query_create_time_begin=request.POST.get('create_time_begin')
    query_create_time_end=request.POST.get('create_time_end')
    if request.method=='POST':     #判断调用的方法
        print "----in post----"
        if query_id!='' or query_car_name!='' or query_photo_url!='' or query_car_groupId!='' or query_car_isPass!='' \
                    or query_deviceType!='' or query_buildId!='' or query_create_time_begin!='' or query_create_time_end!='': #判断是否传了查询参数
            print "----in filter----"
            filter={}      #添加filter参数
            if query_id:
                filter['id'] = query_id
            if query_car_name:
                filter['car_name'] = query_car_name
            if query_photo_url:
                filter['photo_url'] = query_photo_url
            if query_car_groupId:
                filter['car_groupId'] = query_car_groupId
            if query_car_isPass:
                filter['car_isPass'] = query_car_isPass
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
            try:
                print "----in query----"
                result=Photo.objects.filter(**filter) #根据filter查询
                print filter
                p=result.count() #获取查询数据的条数
            except ObjectDoesNotExist, Argument:
                print Argument
            if p!=0: #如果数据大于0条
                list=deal_query_set(result)
                #return render(request,"success.html",{'events':list})
                return JsonResponse({'total':p,'STATUS': 1, 'message': '查询成功','date':list}, json_dumps_params={'ensure_ascii': False})# 数据条数大于0返回条数和list
            else:
                return JsonResponse({'STATUS': -1, 'message': '查询无结果'}, json_dumps_params={'ensure_ascii': False})#数据条数等于0，返回无结果
        else:
            if request.POST:
                return JsonResponse({'STATUS': -1, 'message': '不合法字段2'}, json_dumps_params={'ensure_ascii': False})
            else:
                result=Photo.objects.all()
                p=result.count()
                list=deal_query_set(result)
                return JsonResponse({'total':p,'STATUS': 1, 'message': '查询成功','date':list}, json_dumps_params={'ensure_ascii': False})# 数据条数大于0返回条数和list
    else:

        return JsonResponse({'STATUS': -2, 'message': '非法访问'}, json_dumps_params={'ensure_ascii': False})#提交方式部位post，返回非法访问

