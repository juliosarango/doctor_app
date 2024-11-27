from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailability,
    MedicalNoteSerializer,
    DoctorAvailabilitySerializer,
)
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from .permisions import IsDoctor


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsDoctor]

    @action(detail=True, methods=["POST"], url_path="set-on-vacation")
    def toggle_is_on_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response("El doctor está de vacaciones")

    @action(detail=True, methods=["POST"], url_path="set-off-vacation")
    def toggle_off_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response("El doctor NO está de vacaciones")


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class MedicalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
