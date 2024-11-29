from datetime import date
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from rest_framework import serializers

from bookings.serializers import AppointmentSerializer


class DoctorSerializer(serializers.ModelSerializer):

    appointments = AppointmentSerializer(many=True, read_only=True)

    experience = serializers.SerializerMethodField()

    def get_experience(self, obj) -> int:
        return date.today().year - obj.graduation_date.year

    class Meta:
        model = Doctor
        fields = [
            "id",
            "first_name",
            "last_name",
            "qualification",
            "contact_number",
            "graduation_date",
            "experience",
            "email",
            "address",
            "biography",
            "is_on_vacation",
            "appointments",
        ]

    def validate_email(self, value):
        # Validar campos específicos. En este caso email
        if value.endswith("@gmail.com"):
            return value
        raise serializers.ValidationError("El email debe ser de @gmail.com")

    def validate(self, attrs):
        # Podemos acceder a todos los campos del modelo
        if len(attrs["contact_number"]) < 6 and attrs["is_on_vacation"] == True:
            raise serializers.ValidationError(
                "Por favor ingresa un número de contacto válido antes de irte de vacaciones"
            )
        return super().validate(attrs)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = "__all__"


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = "__all__"
