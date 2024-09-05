app m7_python
proyecto my_site

# Pasos para crear el proyecto
1. Crear entorno virtual
```
virtualenv venv
```
2. Conectarse entorno virtual
```
source venv/Scripts/activate
```
3. Instalar django
```
pip install django
```
4. variables de entorno
pip install python-dotenv

5. postgres
pip install psycopg2

4. Crear el proyecto
```
django-admin startproject my_site .
```
5. Crear la app
```
python manage.py startapp m7_python
```
5. Agregar m7_python en settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'm7_python'
]
```
7. Instalar módulo para trabajar con postgres
```
pip install psycopg2
```
12. Implementar variables de entorno
```bash
pip install python-decouple
```
12. Incluir en sEttings.py
```
from decouple import config # type ignore
```
8. Agregar los requerimientos
```bash
pip freeze > requirements.txt
```
9. Crear base de datos en consola shell
```
CREATE DATABASE m7_python;
\c  m7_python;
```
10. Crear modelos en archivo models.py
```
python manage.py makemigrations
python manage.py migrate

\dt;
SELECT * FROM testdb_adltest;
```
11. Crear usuario y contraseña
```bash
python manage.py createsuperuser
admin
Nico1017
```

5. Conectarse a la shell de django
```
python manage.py shell

from m7_python.models import Comuna,UserProfile,User,Solicitud,Inmueble,Region
from datetime import date

from m7_python.services import crear_usuario,crear_region,crear_comuna,crear_inmueble,listar_propiedades

User.objects.get(id=2).delete()
```
6. Usemos las funciones
```
u1 = crear_usuario(username='nico10',first_name='Nicol',last_name='Matu',email='nico@gmail.com',password='1234')
r1 = crear_region(cod_region='5',nombre_region='Metropolitana')
c1 = crear_comuna(cod_comuna='21',nombre_comuna='Maipu',region_id='5')

c = crear_comuna(cod_region='5',nombre_region='Metropolitana',cod_comuna='21',nombre_comuna='Maipu')

i1 = crear_inmueble(nombre='casa1',descripcion='amplia casa ubicada en pleno centro de la comuna', m2_construidos=114,m2_totales=150,num_estacionamientos=1,num_habitaciones=3,num_baños=2,direccion='Chacabuco #144',tipo_inmueble='casa',precio=100000000,precio_ufs=320,disponible=True,comuna_id='21',arrendador_id=2)

ver_propiedades = listar_propiedades()
----------
v1 = crear_vehiculo(patente='1234',marca='ford',modelo='F-150',year=2015,activo=True)
v2 = crear_vehiculo(patente='4569',marca='fiat',modelo='500',year=2021,activo=True)
v3 = crear_vehiculo(patente='7885',marca='toyota',modelo='T-78',year=2010,activo=True)

c1 = crear_chofer(rut='123456',nombre='eduardo',apellido='perez',activo=True,creacion_registro=date(2021,1,8),vehiculo_id='1234')
c2 = crear_chofer(rut='147852',nombre='camilo',apellido='donoso',activo=True,creacion_registro=date(2022,4,3),vehiculo_id='7885')

r1 = crear_registro_contable(fecha_compra=date(2021,1,9),vehiculo_id='1234',valor=30000)
r2 = crear_registro_contable(fecha_compra=date(2015,4,19),vehiculo_id='4569',valor=870000)

deshabilitar_chofer =deshabilitar_chofer(rut='123456')

obtener_vehiculo = obtener_vehiculo('1234')
print(obtener_vehiculo)

obtener_chofer = obtener_chofer(rut='123456')
print(obtener_chofer)

v3.chofer.nombre
```

7. Para eliminar registros
```
Chofer.objects.filter(rut='123456').delete()
Vehiculo.objects.get().delete()
``` 

## HITO 2

8. Creamos archivo temp.py

9. Poblar datos a partir de la app
```
python manage.py loaddata m7_python/data/users.json
python manage.py loaddata m7_python/data/regiones_comunas.json

```