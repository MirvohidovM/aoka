from django.urls import path

from .views import (LidershipListView,
                    CentralApparatusListView,
                    RegionalAdministrationListView,
                    PressSecretaryAPIView, )


urlpatterns = [
    path('lidership/', LidershipListView.as_view()),
    path('central_apparatus/', CentralApparatusListView.as_view()),
    path('regional_admin/', RegionalAdministrationListView.as_view()),
    path('press-secretary/<int:pk>', PressSecretaryAPIView.as_view()),
]