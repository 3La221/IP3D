
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', views.home, name='home'),
path('add_data/', views.add_data, name='add_data'),


]

