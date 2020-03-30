from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.weixin_main),
    # path('token/', views.token),
    path('menu/', views.createMenu),
    path('userinfo/', views.userinfo),
    path('getUnNormalUser/', views.getUnNormalUser),
    path('table/', views.table),
    path('retable/', views.retable),
    path('submit/', views.submit),
    path('monitor/', views.monitor),
    path('sendMessage/', views.sendMessage)
]
