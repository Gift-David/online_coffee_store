from django.urls import path
from .views import menu_list

urlpatterns = [
    path('', menu_list, name='menu_list'),
    path('user/', menu_list, name=''),
    path('user/view-profile/<int:pk>/', menu_list, name=''),
    path('user/edit-profile/<int:pk>/', menu_list, name=''),
    path('admin/menu/add-menu/', menu_list, name=''),
    path('admin/menu/edit-menu/<int:pk>/', menu_list, name=''),
    path('admin/menu/delete-menu/<int:pk>/', menu_list, name=''),
    path('admin/order/', menu_list, name=''),
]