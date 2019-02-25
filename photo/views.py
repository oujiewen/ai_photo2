# -*-coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
import os
from fileUtil import *
import openpyxl
from models import Photo

def index(requset):

    return render(requset,'index.html')

def upload(requset):
    f1=requset.FILES['txt']
    if f1:
        path=saveExcel(requset)
        t=excelUtil(path)
        savePhoto(t.readExcel(1,None))
        return JsonResponse({'STATUS': 1, 'message': '上传成功'}, json_dumps_params={'ensure_ascii': False})
        response.setContentType("text/html;charset=utf-8");
    else:
        return JsonResponse({'STATUS': -1, 'message': '文件内容为空'}, json_dumps_params={'ensure_ascii': False})
    response.setContentType("text/html;charset=utf-8");

def saveExcel(res):
    uploadExcel=res.FILES['txt']
    if uploadExcel:
        saveExcelPath=settings.TXT_ROOT+"/"+uploadExcel.name
        saveExcel=open(saveExcelPath,'wb')
        for line in uploadExcel.chunks():
            saveExcel.write(line)
            saveExcel.closed
        return saveExcelPath
    
def savePhoto(list):
    try:
        for x in list:
            if x:
                url=x[0].encode('utf-8')
                car_name=x[1].encode('utf-8')
                car_id=x[2]
                device=x[3]
                build=str(x[4])
                isPass=x[5]
                Photo.objects.create(photo_url=url,car_name=car_name,car_groupId=car_id,deviceType=device,buildId=build,isPass=isPass)
    except:
                return JsonResponse({'STATUS': -1, 'message': '文件格式不对'}, json_dumps_params={'ensure_ascii': False})
                response.setContentType("text/html;charset=utf-8");