from django.urls import path
from . import views

urlpatterns = [
 
   # Generic class view
   path('create/', views.product_create_view),  # class method
   path('list/', views.product_list_view, name = 'product-list'),
   path('listcreate/', views.product_list_create_view, name = 'product-list-create'),
   path('<int:pk>/', views.product_detail_view, name = 'product-detail'),  # class method
   path('<int:pk>/update/', views.product_update_view, name = 'product-edit'),
   path('<int:pk>/delete/', views.product_delete_view), 

    # function views
     
    # path('<int:pk>/', views.product_alt_view),  # function method
    # path('', views.product_alt_view),   # function method
    # path('list/', views.product_alt_view),
    # path('listcreate/', views.product_alt_view),

    # mixin views

#    path('create/', views.product_mixin_view), # mixin class method
#    path('list/', views.product_mixin_view),
#    path('<int:pk>/', views.product_mixin_view),  
#    path('<int:pk>/update/', views.product_mixin_view),
#    path('<int:pk>/delete/',views.product_mixin_view),

]