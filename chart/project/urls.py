from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('save_json',views.save_json,name='save_json'),
    path('get',views.get,name="get"),
    path('get_detail/<int:pk>',views.get_detail),
    path('delete/<int:pk>',views.delete),
    path('update/<int:pk>',views.update),
    path('create',views.create)
]