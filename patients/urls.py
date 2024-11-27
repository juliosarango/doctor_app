from django.urls import path
from rest_framework.routers import DefaultRouter
from patients.views import ListPatientsView, DetailPatientView
from .viewsets import PatientViewSet

router = DefaultRouter()
router.register("patients", PatientViewSet)


urlpatterns = router.urls
