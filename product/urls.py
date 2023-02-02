from django.urls import path
from . import views

urlpatterns = [
    path('product-create/', views.ProductCreateAPIView.as_view()),
    path('product-list/', views.ProductListAPIView.as_view()),
    path('product-detail/<str:title>/', views.ProductDetailAPIView.as_view()),
    path('product-update/<str:title>/', views.ProductUpdateAPIView.as_view()),
    path('product-delete/<str:title>/', views.ProductDeleteAPIView.as_view()),

]


