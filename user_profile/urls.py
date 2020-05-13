from django.urls import path
from user_profile import views
urlpatterns = [
    path('',views.index, name='user_profile'),
    # path('<slug:slug>/', views.post_detail, name='post_detail'),#link to be added
    # path('', views.post_detail, name='post_detail'),#link to be added
]