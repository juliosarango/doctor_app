from django.urls import path

from patients.views import ListPatientsView, DetailPatientView

urlpatterns = [
    path("patients/", ListPatientsView.as_view()),
    path("patients/<int:pk>/", DetailPatientView.as_view()),
]
