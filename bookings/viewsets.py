from rest_framework import viewsets
from .serializers import AppointmentSerializer, MedicalNoteSerializer
from .models import Appointment, MedicalNote


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class MedicalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
