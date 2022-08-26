from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index-page'),
    path('predictions',views.prediction,name="cancerapp-prediction")
]