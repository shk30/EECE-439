from django.urls import path
from .views import contact_list, contact_detail, contact_create, contact_update, contact_delete

urlpatterns = [
    path('contacts/', contact_list, name='contact_list'),
    path('contact/<int:pk>/', contact_detail, name='contact_detail'),
    path('contact/create/', contact_create, name='contact_create'),
    path('contact/<int:pk>/update/', contact_update, name='contact_update'),
    path('contact/<int:pk>/delete/', contact_delete, name='contact_delete'),
]
