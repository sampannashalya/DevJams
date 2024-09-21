from django.urls import path
from django.contrib import admin

from . import views

urlpatterns= [
    path("",views.home,name="home"),
    path("/volenteering",views.get_volenteering,name="volenteering"),
    path("/teaching/information",views.teaching_info,name="teaching_info"),
    path("/volenteer/information",views.volenteer_info,name="volenteer_info"),
    path("/teaching",views.teachers,name="teaching"),
    path("/education",views.education,name="education")

]