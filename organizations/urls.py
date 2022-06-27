from django.urls import path

from organizations import views


urlpatterns = [
    path('homepage/', views.OrganizationListView.as_view()),
    path('<slug>', views.OrganizationDetailView.as_view()),
]
