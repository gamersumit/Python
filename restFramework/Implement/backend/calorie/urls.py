from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.CalorieChart_create_view, name = 'add_item'),
    path('list/', views.CalorieChart_list_view, name = 'all_items'),
    path('<int:pk>/', views.CalorieChart_detail_view, name = 'get_item'),
    path('<int:pk>/update/', views.CalorieChart_update_view, name = 'update_item'),
    path('<int:pk>/delete/', views.CalorieChart_delete_view, name = 'delete_item'),
]