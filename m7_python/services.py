from .models import Comuna,UserProfile,User,Solicitud,Inmueble,Region

def get_or_create_user_profile(user):
    try:
        # Intenta obtener el perfil del usuario o crearlo si no existe
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            print("Se ha creado un nuevo perfil para el usuario.")
        else:
            print("El perfil ya existía.")
        return user_profile
    except Exception as e:
        print(f'Error al obtener o crear el perfil del usuario. {e}')
        return None
    
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

def actualizar_disponibilidad_inmueble(id,disponible):
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

def get_all_inmuebles():
    try: 
        inmuebles = Inmueble.objects.filter(disponible=True) 
        return inmuebles 
    except Exception as e: 
        print(f"Error al obtener los inmuebles: {str(e)}")
        return []


def get_inmuebles_for_arrendador(user):
    rol = user.user_profile.rol 
    if rol != 'arrendador':
        print(f'no es arrendador')
        return [] 
    inmuebles = Inmueble.objects.filter(arrendador=user)
    if not inmuebles.exists():
        print(f'no hay inmuebles')
        return []
    return inmuebles

def create_inmueble_for_arrendador(user, data):
    new_inmueble = Inmueble(**data)
    new_inmueble.arrendador = user 
    new_inmueble.save()
    return new_inmueble