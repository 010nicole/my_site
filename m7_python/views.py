from django.shortcuts import render, redirect, get_object_or_404
from .services import get_all_inmuebles, get_or_create_user_profile, get_inmuebles_for_arrendador,create_inmueble_for_arrendador, actualizar_disponibilidad_inmueble
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserProfileForm, ContactModelForm, UserForm, UserEditProfileForm, InmuebleForm, EditDisponibilidadForm
from .models import UserProfile, ContactForm, Inmueble, Solicitud, User
from django.contrib.auth import login
from django.contrib import messages  # type: ignore
from .decorators import rol_requerido

# Create your views here.

#* Route para manejo de NOT_AUTH
def not_authorized_view(request):
    return render(request, "not_authorized.html", {})


@login_required
def indexView(request):
    if request.user.is_authenticated:
        profile = get_or_create_user_profile(request.user)
        if profile.rol == 'arrendador':
            messages.success(request,'arrendador')
            return redirect('dashboard_arrendador')
        elif profile.rol == 'arrendatario':
            messages.success(request,'arrendatario')
            return redirect('index_arrendatario')
        else:
            return redirect('login')
        # inmuebles = get_all_inmuebles()
        # return render(request,'index.html',{'inmuebles':inmuebles} )
    else:
        return redirect('login')

@login_required
def index_arrendatario(request):
    inmuebles = get_all_inmuebles()
    return render(request,'arrendatario/index_arrendatario.html',{'inmuebles':inmuebles} )

@login_required
def dashboard_arrendador(request):
    inmuebles = get_inmuebles_for_arrendador(request.user)
    return render(request,'arrendador/dashboard_arrendador.html',{'inmuebles':inmuebles} )



# STEP -> CREAR el FORM de Registro
#TODO__ REGISTER and REGISTER_ROL (tipo de usuario) - FORMS
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('register_rol')
    else:
        form = CustomUserCreationForm()
    return render(request,'registration/register.html',{'form':form} )

@login_required
def register_rol(request):
    user_profile = get_or_create_user_profile(request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio o cualquier otra página
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'registration/register_rol.html', {'form': form})


#* VER PERFIL
@login_required
def profile_view(request):
    user = request.user
    user_profile = get_or_create_user_profile(user)  # Llama al servicio para obtener o crear el perfil

    if not user_profile:
        # En caso de que ocurra un error al obtener o crear el perfil
        return render(request, 'error.html', {'message': 'No se pudo obtener el perfil del usuario.'})

    return render(request, 'profile_detail.html', {
        'user': user,
        'profile': user_profile,
    })

#* EDITAR PERFIL -> UserForm, UserEditProfileForm
@login_required
def edit_profile_view(request):
    user = request.user 
    user_profile = get_or_create_user_profile(user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserEditProfileForm(request.POST, instance=user_profile) 
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else: # GET
        user_form = UserForm(instance=user) 
        profile_form = UserEditProfileForm(instance=user_profile)
    return render(request, 'profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def about(request):
    return render(request, 'about.html', {})

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST) # <- {"customer_email": "kiki@gamial.com", "customer_name": "Kiki", "message": "Hola soy Kiki"}
        print(f'errors -> {form.errors}')
        if form.is_valid():
            #* MODEL - Guardamos la data en nuestra DB en la TABLA CONACTFORM
            ContactForm.objects.create(**form.cleaned_data) # pasamos la data del diccionario .cleaned_data a argumentos
            # messages.success(request, f'Gracias por contactarse con nosotros, en breve le responderemos.')
            return redirect('home')
    else: 
        form = ContactModelForm()   
    return render(request, 'contact.html', {'form':form})


#TODO__ ARRENDADOR - VIEWS

@login_required
@rol_requerido('arrendador')
def create_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = create_inmueble_for_arrendador(request.user, form.cleaned_data)
            return redirect('dashboard_arrendador')
    else: 
        form = InmuebleForm()
    return render(request, 'arrendador/create_inmueble.html', {'form': form})

@login_required
def edit_inmueble(request, inmueble_id):
    inmueble_edit =  get_object_or_404(Inmueble, id=inmueble_id)
    # inmueble_edit =  Inmueble.objects.get(pk=inmueble_id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble_edit)
        if form.is_valid():
            #* Crear service para update Inmueble y validar
            form.save()
            return redirect('dashboard_arrendador')
    else: 
        form = InmuebleForm(instance=inmueble_edit)
    return render(request, 'arrendador/edit_inmueble.html', {'form': form})

@login_required
def detail_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    # inmueble =  Inmueble.objects.get(id=inmueble_id)
    return render(request, 'detail_inmueble.html', {'inmueble': inmueble})

@login_required
def delete_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('dashboard_arrendador')

    return render(request, 'arrendador/delete_inmueble.html', {'inmueble': inmueble})

@login_required
def detail_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    # inmueble =  Inmueble.objects.get(id=inmueble_id)
    return render(request, 'detail_inmueble.html', {'inmueble': inmueble})

@login_required
def edit_disponibilidad_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        form = EditDisponibilidadForm(request.POST, instance=inmueble) 
        if form.is_valid():
            disponible = form.cleaned_data['disponible']
            result = actualizar_disponibilidad_inmueble(inmueble_id, disponible)
            if result["success"]:
                messages.success(request, result["message"])
            else: 
                messages.error(request, result["message"])
            return redirect('dashboard_arrendador')
             
    else: 
        form = EditDisponibilidadForm(instance=inmueble)
    return render(request, 'arrendador/edit_disponibilidad.html', {'form': form, 'inmueble': inmueble})


#TODO__ ARRENDATARIOS - VIEWS

@login_required
@rol_requerido('arrendatario')
def send_solicitud(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        solicitud = Solicitud(arrendatario= request.user, inmueble= inmueble, estado= 'pendiente')
        solicitud.save()
        messages.success(request, f'Solicitud inmueble {inmueble.nombre} realizada con éxito!!!')
        return redirect('index_arrendatario')
    return render(request, 'arrendatario/send_solicitud.html', {'inmueble': inmueble})

def view_list_user_solicitudes(request):
    
    arrendatario =  get_object_or_404(User, id=request.user.id)
    solicitudes = Solicitud.objects.filter(arrendatario=arrendatario)
    return render(request, 'arrendatario/list_user_solicitudes.html', {
        'solicitudes': solicitudes,
        'arrendatario': arrendatario
    })
