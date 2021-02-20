from django.urls import path
from . import views

urlpatterns=[
    path('mains',views.search,name="mains"),
    path('upload',views.uppdf,name="upload"),
]