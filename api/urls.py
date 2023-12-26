from django.urls import path,include
from rest_framework import routers
from api.views import api_MVS


rout=routers.DefaultRouter()
rout.register(r'customers',api_MVS)

urlpatterns = [
    path('',include(rout.urls))
]
