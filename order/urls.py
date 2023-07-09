
from django.urls import path
from . import views

urlpatterns = [

    path('',views.list_orders),
    path('add_order/',views.add_order,name="add_order"),
    path('update_order/<str:pk>',views.update_order,name="update_order"),
    path('delete_order/<str:pk>',views.delete_order, name="delete_order")
]
