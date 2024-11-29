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

## Creando nuestras views

- Functions View
- APIView
- Generic Views
### Ventajas de usar Generic Views
- Reducción de código repetitivo: Implementaciones predefinidas para operaciones comunes.
- Mejora de consistencia y mantenibilidad: Aplicación de patrones uniformes en toda la API.
- Aceleración del desarrollo: Permite centrarse en la lógica específica de la aplicación.
- Facilidad de integración y extensión: Composición de comportamientos reutilizables.
- Promoción de buenas prácticas: Adherencia a los principios de diseño de Django y REST.

Toda la documentación de las generic views está disponible en la siguiente [url](https://www.cdrf.co/)

### ViewSets
Los Viewsets en DRF nos ayudan a simplificar la creación de vistas al reutilizar una clase que agrupa el código necesario para manejar diferentes operaciones sobre un recurso, como listar, crear, actualizar y eliminar. Al integrarlos con los routers, evitamos la necesidad de definir cada URL manualmente, ya que el router se encarga de generar todas las rutas de manera automática.

## Throttling
Limitar las solicitudes a una API es fundamental para evitar abusos y proteger los recursos del servidor. El throttling es una técnica clave en este proceso, ya que permite controlar la cantidad de solicitudes que diferentes usuarios pueden hacer en un determinado periodo, previniendo ataques como DDoS y optimizando el rendimiento.

- Primero, debemos entender que el throttling se configura de manera similar a los permisos y autenticación.
- Definimos límites como “requests por segundo, minuto, hora o día”, y estos valores pueden ser diferentes para usuarios anónimos o autenticados.
La configuración básica se verí así:
```
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '100/minute'
    }
}
```
En la configuración anterior, estamos estableciendo los siguientes límites:
- 10 solicitudes por minuto para usuarios anónimos.
- 100 solicitudes por minuto para usuarios autenticados.

## Pruebas unitarias
Las pruebas unitarias son esenciales para garantizar que nuestras APIs funcionen correctamente sin tener que gastar demasiados recursos. Django REST Framework facilita este proceso mediante la clase APIClient, que nos permite simular requests y validar los resultados de forma sencilla y eficiente. 
El cliente APIClient es esencial para nuestras pruebas ya que simula requests HTTP, permitiéndonos probar las respuestas de nuestra API sin hacer requests reales. Esto nos ahorra tiempo y recursos. Además, se configura automáticamente para trabajar con datos JSON, simplificando las pruebas.

Para ejecutar las pruebas unitarias ejecutamos el comando ```python manage.py test```
```
(venv) [jsarangoq@jsar-d9845-uio DRF]$ python manage.py test 
Found 7 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 2.102s

OK
Destroying test database for alias 'default'...
(venv) [jsarangoq@jsar-d9845-uio DRF]$ 
```
En las líneas anteriores podemos ver que se ejecutaron 7 tests y que el tiempo de ejecución es de 2.102s.

### Code Coverage
Para obtener el código de cobertura de nuestro proyecto, ejecutamos el siguiente comando:
```
coverage run manage.py test 
coverage report
```
```
(venv) [jsarangoq@jsar-d9845-uio DRF]$ coverage report
Name                      Stmts   Miss  Cover
---------------------------------------------
bookings/serializers.py      10      0   100%
bookings/viewsets.py          9      0   100%
doctors/permisions.py         4      0   100%
doctors/serializers.py       32      0   100%
doctors/viewsets.py          48      0   100%
patients/serializers.py      20      0   100%
patients/views.py            16      0   100%
patients/viewsets.py          6      0   100%
---------------------------------------------
TOTAL                       145      0   100%
```

## Documentación de API's
Usaremos la librería [drf-spectacular](https://www.drf-spectacular.readthedocs.io/en/latest/index.html) para generar nuestra documentación de API's.
```
pip install drf-spectacular
```
Luego de configurada la librería drf-spectacular, esta nos permite generar la documentación con el estándar [OpenAPI](https://www.openapis.org/). Podemos acceder a la documentación de la API desde el navegador, tanto con swagger como con redoc.

### Documentación de la API con Swagger
![Swagger](images/swagger.png)

### Documentación de la API con Redoc
![Redoc](images/redocs.png)

## Links de interés
- [Documentación de drf-spectacular](https://www.drf-spectacular.readthedocs.io/en/latest/index.html)
- [Documentación de django-rest-framework](https://www.django-rest-framework.org/)
- [Documentación de coverage](https://coverage.readthedocs.io/en/7.6.8/)    
- [Django](https://www.djangoproject.com/)