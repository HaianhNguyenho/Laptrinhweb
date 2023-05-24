from django.urls import path
from.import views
app_name='home'

urlpatterns = [
    
    path('', views.get_index),
    path('form/', views.get_formsv.as_view, name='form'),
]