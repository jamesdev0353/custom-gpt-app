from django.urls import path
from . import views

app_name = 'xhatgpt'

urlpatterns = [
    path('',views.query,name="xhatgpt"), # can use name for link refering, 'xhatgpt:xhatgpt'
    path('/About',views.about,name="aboutx") # 'xhatgpt:aboutx'
]