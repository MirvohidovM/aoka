from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListAPIView.as_view()),
    path('<slug>', views.NewsRetrieveAPIView.as_view()),
    path('threenews/', views.NewsThreeListAPIView.as_view()),
    path('main_new/', views.NewsOneMainAPIView.as_view()),
]
