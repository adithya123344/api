from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import userViewSet
from .views import Showsingle, userViewSet
from  api import views as apiview
from . import views 

router = routers.DefaultRouter()
router.register('users',userViewSet)

urlpatterns = [
    
    path('api',include(router.urls)),
    path('status/',views.ShowAll,name='deskstatus'),
    path('status/<str:pk>/',views.Showsingle,name='singledisk'),
    path('status/<str:pk>/update/',views.Updatesingle,name='updatedesk')

]
