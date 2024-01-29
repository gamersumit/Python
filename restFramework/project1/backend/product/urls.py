from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.product_detail_view),
    path('', views.product_create_view),
    path('list/', views.product_list_view),
    path('listcreate/', views.product_list_create_view),
]