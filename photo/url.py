from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib import admin
from photo import views
from photo import query
from photo import uploadPic
from photo import queryUtil
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^upload/', views.upload),
    url(r'^uploadPic/', uploadPic.uploadPic),
    url(r'^query/', query.query_photo),
    url(r'^queryAdmin/', queryUtil.queryPhotoAdmin),
    url(r'^delete/(\d+)/$', queryUtil.deletePhoto),
    url(r'^(\d+)/$', queryUtil.getPhoto),
    url(r'^addphoto/', queryUtil.addPhoto),
    url(r'^updatephoto/(\d+)/', queryUtil.updatePhoto),

]
