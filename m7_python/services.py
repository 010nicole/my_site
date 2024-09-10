from .models import Comuna,UserProfile,User,Solicitud,Inmueble,Region

def crear_usuario(username,first_name,last_name,email,password):
    usuario = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
    return usuario

def crear_region(cod,nombre):
    region = Region.objects.create(cod=cod,nombre=nombre)
    return region

def crear_comuna(cod_comuna,nombre_comuna,region_id):
    region = Region.objects.get(cod=region_id)
    comuna = Comuna.objects.create(cod=cod_comuna,nombre=nombre_comuna,region=region)
    return comuna

def crear_inmueble(nombre,descripcion, m2_construidos,m2_totales,num_estacionamientos,num_habitaciones,num_baños,direccion,tipo_inmueble,precio,precio_ufs,cod_comuna,arrendador_id):
    arrendador = User.objects.get(cod_comuna=arrendador_id)
    comuna = Comuna.objects.get(cod_comuna=cod_comuna)
    inmueble = Inmueble.objects.create(nombre=nombre,descripcion=descripcion, m2_construidos=m2_construidos,m2_totales=m2_totales,num_estacionamientos=num_estacionamientos,num_habitaciones=num_habitaciones,num_baños=num_baños,direccion=direccion,tipo_inmueble=tipo_inmueble,precio=precio,precio_ufs=precio_ufs,comuna=comuna,arrendador=arrendador)
    return inmueble

def listar_propiedades():
    propiedad = Inmueble.objects.all()
    return {
                'success':True,
                'data': propiedad
            }

def actualizar_disponibilidad(id,disponible):
    try:
        inmueble = Inmueble.objects.get(id=id)
        inmueble.disponible = disponible
        inmueble.save()
        return {
            'success': True,
            'message': "Disponibilidad actualizada"
        }
    except Inmueble.DoesNotExist:
        return {
            'success': False,
            'message': "Inmueble no encontrado"
        }
    except Exception as e:
        return {
            'success': False,
            'message': "Error al actualizar disponibilidad"
        }

def eliminar_inmueble(id):
    try:
        inmueble = Inmueble.objects.get(id=id)
        inmueble.delete()
        return {
            'success': True,
            'message': "Inmueble eliminado"
        }
    except Inmueble.DoesNotExist:
        return {
            'success': False,
            'message': "Inmueble no encontrado"
        }
    except Exception as e:
        return {
            'success': False,
            'message': "Error al eliminar inmueble"
        }
        
# def crear_comuna(cod_region,nombre_region,cod_comuna,nombre_comuna):
#     region = Region.objects.create(cod=cod_region,nombre=nombre_region)
#     comuna = Comuna.objects.create(cod=cod_comuna,nombre=nombre_comuna)
#     comuna.region = region
#     comuna.save()
#     return comuna