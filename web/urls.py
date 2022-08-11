from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('QAlibrary',views.QAlibrary,name='QAlibrary'),
    path('donation',views.donation,name='donation'),
    path('homecare',views.homecare,name='homecare'),
    ]