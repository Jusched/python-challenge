# Django modules
from django.urls import path

# Local modules
from .views import views
  

urlpatterns = [
    path('', views.ApiView, name="all-views"),
    path('create/', views.add_booking, name="add-booking"),
    path('view/<int:pk>', views.view_booking, name="view-booking"),
    path('update/<int:pk>/', views.update_booking, name='update-booking'),
    path('delete/<int:pk>/', views.delete_booking, name='delete-booking'),
]
