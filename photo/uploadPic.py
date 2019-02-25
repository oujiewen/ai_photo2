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


def uploadPic(res):
    uploadExcel=res.FILES['txt']
    if uploadExcel:
        saveExcelPath=settings.TXT_ROOT+"/"+uploadExcel.name
        saveExcel=open(saveExcelPath,'wb')
        for line in uploadExcel.chunks():
            saveExcel.write(line)
            saveExcel.closed
        return saveExcelPath