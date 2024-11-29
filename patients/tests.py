from django.test import TestCase

from datetime import date
from django.urls import reverse
from django.test import TestCase
from patients.models import Patient
from .models import Patient

from rest_framework.test import APIClient
from rest_framework import status


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

        self.client = APIClient()

    def create_patients_response_201(self):
        data = self.client = {
            "first_name": "Cliente",
            "last_name": "De prueba",
            "date_of_birth": "2000-12-12",
            "contact_number": "123456",
            "email": "cliente@gmail.com",
            "address": "Barrio de la Paz, 1",
            "medical_history": "Covid, hipertensión, diabetes",
        }

        url = reverse("patient-list")

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_should_return_200(self):
        url = reverse("patient-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_should_return_200(self):
        url = reverse("patient-detail", kwargs={"pk": self.patient.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_should_return_404(self):
        url = reverse("patient-detail", kwargs={"pk": 1000})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
