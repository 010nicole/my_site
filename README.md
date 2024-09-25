app m7_python
proyecto my_site
## HITO 1

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
SELECT * FROM m7_python_inmueble;
```
11. Crear usuario y contraseña
```bash
python manage.py createsuperuser
admin
Nico1017
```

12. Probar el proyecto ingresando como admin
```bash
python manage.py runserver
```

13. Conectarse a la shell de django
```
python manage.py shell
```
from m7_python.models import Comuna,UserProfile,User,Solicitud,Inmueble,Region
from datetime import date
```
from m7_python.services import crear_usuario,crear_region,crear_comuna,crear_inmueble,listar_propiedades,actualizar_disponibilidad,eliminar_inmueble
```
from m7_python.temp import get_list_inmuebles_sql

13. Usemos las funciones
```
u1 = crear_usuario(username='nico10',first_name='Nicol',last_name='Matu',email='nico@gmail.com',password='1234')
r1 = crear_region(cod_region='5',nombre_region='Metropolitana')
c1 = crear_comuna(cod_comuna='21',nombre_comuna='Maipu',region_id='5')
```
c = crear_comuna(cod_region='5',nombre_region='Metropolitana',cod_comuna='21',nombre_comuna='Maipu')
```
i1 = crear_inmueble(nombre='casa1',descripcion='amplia casa ubicada en pleno centro de la comuna', m2_construidos=114,m2_totales=150,num_estacionamientos=1,num_habitaciones=3,num_baños=2,direccion='Chacabuco #144',tipo_inmueble='casa',precio=100000000,precio_ufs=320,disponible=True,comuna_id='21',arrendador_id=2)
```
ver_propiedades = listar_propiedades()


## HITO 2
1. Poblar datos a partir de la app
```
python manage.py loaddata m7_python/data/users.json
python manage.py loaddata m7_python/data/regiones_comunas.json
python manage.py loaddata m7_python/data/inmuebles.json
```

2. Creamos archivo temp.py

3. Corremos el archivo temp.py
```
python m7_python/temp.py
```

## HITO 3
1. Formularios `login` y `logout`
    - `registration/login`
    - `registration/logout`
```bash
 path('login/',LoginView.as_view(),name='login_url'), # FORMS
 path('logout/',LogoutView.as_view(next_page='home'),name='logout'), # FORMS
```
`https://docs.djangoproject.com/en/5.1/topics/auth/default/`

2. Armar Estructura Vistas APP (Cuadro - Base + navBar)
    - base.html
        - navbar
        - footer
        - about
        - contact 
        
3. Crear los 2 Formularios necesarios de REGISTRO
```bash
 path('register/',views.registerView,name='register_url'), # FORMS
 path('register_tipo/',views.register_tipoView,name='register_tipo_url'), # FORMS
```
4. Crear la vista de PERFIL y el FORM de edit_PERFIL
```bash
 path('view_profile/',views.profile,name='profile'), # No Forms
 path('udpate_profile/',views.profile,name='update_profile'), # FORMS
```
5. Vistas por adelantar
    - home - Index -> 3 posibilidades   1 (form login + register) 2 Arrendador 3 Arrendatario
    - dashboard_arrendador (filter diferenciado de lista de inmuebles)
    - dashboard_arrendatario  (filter diferenciado de lista de inmuebles)
