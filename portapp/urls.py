from django.urls import path
from portapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success')  # The homepage with the form
]
