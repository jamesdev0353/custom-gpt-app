from django.urls import path
from . import views

app_name = 'xhatgpt'

urlpatterns = [
    path('',views.query,name="xhatgpt"),
    path('/About',views.about,name="aboutx")
]