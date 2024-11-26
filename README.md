# Django Rest Framework - DRF

## Instalación
1. Crear virtualenv
```
python -m venv venv
source venv/bin/activate
```
2. Instalar dependencias
```
pip install -r requirements.txt
```
## Serializers
Los serializadores permiten que datos complejos, como querysets e instancias de modelos, se conviertan en tipos de datos nativos de Python que luego pueden ser fácilmente transformados en JSON, XML u otros tipos de contenido.


```
python manage.py shell-plus
from patients.models import Patient
from patients.serializers import PatientSerializer

data = {"first_name":"Luis","last_name":"MAtinez"}
serializer = PatientSerializer(data=data)
serializer.is_valid()
False
serializer.errors

{'date_of_birth': [ErrorDetail(string='This field is required.', code='required')], 'contact_number': [ErrorDetail(string='This field is required.', code='required')], 'email': [ErrorDetail(string='This field is required.', code='required')], 'address': [ErrorDetail(string='This field is required.', code='required')], 'medical_history': [ErrorDetail(string='This field is required.', code='required')]}
```