from datetime import date
from django.urls import reverse
from django.test import TestCase
from patients.models import Patient
from .models import Doctor

from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User, Group


class DoctorViewSetTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="Juan",
            last_name="Sarango",
            date_of_birth=date(1940, 1, 1),
            contact_number="123456789",
            email="juansarango@gmail.com",
            address="Calle de la Paz, 1",
            medical_history="No tengo historia de medicina",
        )

        self.doctor = Doctor.objects.create(
            first_name="Jorge",
            last_name="Lozano",
            qualification="Medico",
            contact_number="123456789",
            graduation_date=date(2020, 1, 1),
            email="jorge@gmail.com",
            address="Calle de la Paz, 1",
            biography="Medico especialista en cardiología",
            is_on_vacation=False,
        )

        self.group = Group.objects.create(name="doctors")
        self.user = User.objects.create_user(
            username="doctor",
            password="doctor",
        )
        self.user.groups.add(self.group)

        self.client = APIClient()

    def test_list_should_return_403(self):
        url = reverse("doctors-appointments", kwargs={"pk": self.doctor.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_should_return_200(self):
        url = reverse("doctors-appointments", kwargs={"pk": self.doctor.id})
        self.client.login(username="doctor", password="doctor")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_return_doctor_detail(self):
        url = reverse("doctors-detail", kwargs={"pk": self.doctor.id})
        self.client.login(username="doctor", password="doctor")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.doctor.id)

    def test_put_doctor_on_vacation(self):
        url = reverse("doctors-toggle-is-on-vacation", kwargs={"pk": self.doctor.id})
        self.client.login(username="doctor", password="doctor")
        response = self.client.post(url, data={"is_on_vacation": True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "El doctor está de vacaciones")

    def test_put_doctor_off_vacation(self):
        url = reverse("doctors-toggle-off-vacation", kwargs={"pk": self.doctor.id})
        self.client.login(username="doctor", password="doctor")
        response = self.client.post(url, data={"is_on_vacation": False})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "El doctor NO está de vacaciones")

    def test_apointment(self):
        url = reverse("doctors-appointments", kwargs={"pk": self.doctor.id})
        self.client.login(username="doctor", password="doctor")
        appointment = {
            "appointment_date": "2024-01-10",
            "appointment_time": "10:00:00",
            "notes": "Cita agendada",
            "status": "confirmed",
            "patient": self.patient.id,
            "doctor": self.doctor.id,
        }
        response = self.client.post(url, data=appointment)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_apointment_should_return_403(self):
        url = reverse("doctors-appointments", kwargs={"pk": self.doctor.id})
        appointment = {
            "appointment_date": "2024-01-10",
            "appointment_time": "10:00:00",
            "notes": "Cita agendada",
            "status": "confirmed",
            "patient": self.patient.id,
            "doctor": self.doctor.id,
        }
        response = self.client.post(url, data=appointment)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_doctor_validate_contact_number_and_is_on_vacation_should_return_403(
        self,
    ):
        url = reverse("doctors-list")
        self.client.login(username="doctor", password="doctor")
        response = self.client.post(
            url,
            data={
                "first_name": "Juan",
                "last_name": "lopez",
                "qualification": "Medico",
                "contact_number": "12345",
                "graduation_date": "2020-01-01",
                "email": "juanlopez@gmail.com",
                "address": "Calle de la Paz, 1",
                "biography": "Medico especialista en cardiología",
                "is_on_vacation": True,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json()["non_field_errors"][0],
            "Por favor ingresa un número de contacto válido antes de irte de vacaciones",
        )

    def test_create_doctor_validate_email_should_return_403(self):
        url = reverse("doctors-list")
        self.client.login(username="doctor", password="doctor")
        response = self.client.post(
            url,
            data={
                "first_name": "Juan",
                "last_name": "lopez",
                "qualification": "Medico",
                "contact_number": "12345454545",
                "graduation_date": "2020-01-01",
                "email": "juanlopez@example.com",
                "address": "Calle de la Paz, 1",
                "biography": "Medico especialista en cardiología",
                "is_on_vacation": False,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json()["email"][0],
            "El email debe ser de @gmail.com",
        )

    def test_create_doctor_should_return_201(self):
        url = reverse("doctors-list")
        self.client.login(username="doctor", password="doctor")
        response = self.client.post(
            url,
            data={
                "first_name": "Juan",
                "last_name": "lopez",
                "qualification": "Medico",
                "contact_number": "12345454545",
                "graduation_date": "2020-01-01",
                "email": "juanlopez@gmail.com",
                "address": "Calle de la Paz, 1",
                "biography": "Medico especialista en cardiología",
                "is_on_vacation": False,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
