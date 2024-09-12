import os
import django

import sys
# # Asegúrate de que el directorio del proyecto esté en el PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# -> .../OneDrive/Escritorio/DJANGO-PY 2024/MODULOS/MODULO-7/HITO2 

import my_site
# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")
django.setup()

from m7_python.models import Inmueble, Region, Comuna
from django.contrib.auth.models import User

def listado_inmuebles_comuna_orm(comuna,desc=None):
    filtros = {
        'comuna__nombre__icontains':comuna
    }
    if desc:
        filtros['descripcion__icontains'] = desc
    inmuebles = Inmueble.objects.filter(**filtros)
    index = 1
    with open("m7_python/outputs/datos.txt", "a") as file:
        file.write(f'__listado_inmuebles_comuna_orm__\n')
        for l in inmuebles:
            file.write(f"{index}__ {l.nombre}, {l.descripcion} - comuna {l.comuna.nombre}\n")
            index += 1

def listado_inmuebles_comuna_sql(comuna):
    select = """
        SELECT i.id, i.nombre, i.descripcion
        FROM m7_python_inmueble as i
        INNER JOIN m7_python_comuna as c
        on i.comuna_id = c.cod
        WHERE c.nombre ILIKE %s
        """
    inmuebles = Inmueble.objects.raw(select,[f"%{comuna}%"])
    index = 1
    with open("m7_python/outputs/datos.txt", "a") as file:
        file.write(f'__listado_inmuebles_comuna_sql__\n')
        for l in inmuebles:
            file.write(f"{index}__ {l.nombre}, {l.descripcion} - comuna {l.comuna.nombre}\n")
            index += 1

def listado_inmuebles_region_orm(region):
    inmuebles = Inmueble.objects.filter(comuna__region__nombre__icontains=region)
    index = 1
    with open("m7_python/outputs/datos.txt", "a") as file:
        file.write(f'__listado_inmuebles_region_orm__\n')
        for l in inmuebles:
            file.write(f"{index}__ {l.nombre}, {l.descripcion} - region {l.comuna.region.nombre}\n")
            index += 1
            
def listado_inmuebles_region_sql(region):
    select = """
        SELECT i.id, i.nombre, i.descripcion
        FROM m7_python_inmueble as i
        INNER JOIN m7_python_comuna as c
        on i.comuna_id = c.cod
        INNER JOIN m7_python_region as r
        on c.region_id = r.cod
        WHERE r.nombre ILIKE %s
        """
    inmuebles = Inmueble.objects.raw(select,[f"%{region}%"])
    index = 1
    with open("m7_python/outputs/datos.txt", "a") as file:
        file.write(f'__listado_inmuebles_region_sql__\n')
        for l in inmuebles:
            file.write(f"{index}__ {l.nombre}, {l.descripcion} - region {l.comuna.region.nombre}\n")
            index += 1

if __name__ == "__main__":
    listado_inmuebles_comuna_orm("pucón")
    listado_inmuebles_comuna_sql("San Felipe")
    listado_inmuebles_region_orm("De Valparaíso")
    listado_inmuebles_region_sql("De La Araucanía")
    

