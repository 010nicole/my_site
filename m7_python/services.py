from .models import Comuna,UserProfile,User,Solicitud,Inmueble,Region
# uario tipo arrendador debe poder:
# a. Publicar sus propiedades en una comuna determinada con sus
# características.
# def publicar_propiedad():
    
# b. Listar propiedades en el dashboard.
# c. Eliminar y editar sus propiedades.
# d. Aceptar arrendatarios.

def crear_usuario(username,first_name,last_name,email,password):
    usuario = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
    return usuario

def crear_region(cod_region,nombre_region):
    region = Region.objects.create(cod=cod_region,nombre=nombre_region)
    return region

def crear_comuna(cod_comuna,nombre_comuna,region_id):
    comuna = Comuna.objects.create(cod=cod_comuna,nombre=nombre_comuna,region_id=region_id)
    return comuna

def crear_inmueble(nombre,descripcion, m2_construidos,m2_totales,num_estacionamientos,num_habitaciones,num_baños,direccion,tipo_inmueble,precio,precio_ufs,disponible,comuna_id,arrendador_id):
    inmueble = Inmueble.objects.create(nombre=nombre,descripcion=descripcion, m2_construidos=m2_construidos,m2_totales=m2_totales,num_estacionamientos=num_estacionamientos,num_habitaciones=num_habitaciones,num_baños=num_baños,direccion=direccion,tipo_inmueble=tipo_inmueble,precio=precio,precio_ufs=precio_ufs,disponible=disponible,comuna_id=comuna_id,arrendador_id=arrendador_id)
    return inmueble

def publicar_propiedad():
    pass

def listar_propiedades():
    propiedad = Inmueble.objects.all()
    return {
                'success':True,
                'data': propiedad
            }

# def crear_comuna(cod_region,nombre_region,cod_comuna,nombre_comuna):
#     region = Region.objects.create(cod=cod_region,nombre=nombre_region)
#     comuna = Comuna.objects.create(cod=cod_comuna,nombre=nombre_comuna)
#     comuna.region = region
#     comuna.save()
#     return comuna