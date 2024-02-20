from django.contrib import admin
from django.urls import path
from trading import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('warehouse/', views.warehouse),
    path('payment/', views.payment),
    path('about/', views.about),
    path('form/', views.form),

]
