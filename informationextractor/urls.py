from . import views
from django.urls import path, include
urlpatterns = [
    path('', views.home,name='home'),
  #  path('updater/', views.updater,name='updater'),
    
]
