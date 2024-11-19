from django.urls import path
from .views import cellphone_list, cellphone_create, cellphone_update, cellphone_delete

urlpatterns = [
    path('', cellphone_list, name='cellphone_list'),  # This matches the empty path under 'cellphones/'
    path('new/', cellphone_create, name='cellphone_create'),
    path('<int:pk>/edit/', cellphone_update, name='cellphone_update'),
    path('<int:pk>/delete/', cellphone_delete, name='cellphone_delete'),
]