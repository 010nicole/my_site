import os
import django

import sys
# # Asegúrate de que el directorio del proyecto esté en el PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# -> .../OneDrive/Escritorio/DJANGO-PY 2024/MODULOS/MODULO-7/HITO2 

import my_site
# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from m7_python.models import Inmueble, Region, Comuna 
from django.contrib.auth.models import User

#TODO_ Ejemplos SIMPLES:
def get_list_inmuebles_sql():
    select = """
        SELECT * FROM m7_python_inmueble
        """
    inmuebles = Inmueble.objects.raw(select)
    # inmuebles = Inmueble.objects.all()     <- ORM
    index=1
    print("LISTA INMUEBLES")
    for l in inmuebles:
        print(f"{index}__ {l.nombre}, {l.descripcion}")
        index += 1
    with open("m7_python/outputs/datos.txt", "a") as file:
        for l in inmuebles:
            # print(f" {l.nombre}, {l.descripcion}")
            file.write(f" {l.nombre}, {l.descripcion}\n")
                
    return


# Ejecución de funciones de ejemplo
if __name__ == "__main__":
    #TODO_ Ejemplos SIMPLES:
    get_list_inmuebles_sql()
    

