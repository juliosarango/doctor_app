from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import (
    DoctorViewSet,
    DepartmentViewSet,
    DoctorAvailabilityViewSet,
    MedicalNoteViewSet,
)

router = DefaultRouter()
router.register("doctors", DoctorViewSet, basename="doctors")
router.register("departments", DepartmentViewSet)
router.register("doctor-availabilities", DoctorAvailabilityViewSet)
router.register("medical-notes", MedicalNoteViewSet)

urlpatterns = router.urls
