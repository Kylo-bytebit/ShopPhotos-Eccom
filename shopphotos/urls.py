from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('search/', views.search, name='search'),
    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.image_list, name='image_list'),
    path('purchase copy/<str:image_name>/', views.image_purchase, name='purchase'),
    path('images/<int:image_id>/edit/', views.edit_image, name='edit_image'),
    path('images/<int:image_id>/delete/', views.delete_image, name='delete_image'),
    path('purchase/<str:image_title>/', views.image_purchase_v, name='purchase_u'),
    path('add_to_cart/<int:photo_id>/', views.add_to_cart, name='add_to_cart'),
]