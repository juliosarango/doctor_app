from .models import Doctor, Department, DoctorAvailability, MedicalNote
from rest_framework import serializers


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

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
