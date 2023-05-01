from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('sandwiches/', views.sandwich_index, name='index'),
    path('sandwiches/<int:pk>/', views.SandwichDetail.as_view(), name='sandwich_detail'),
]