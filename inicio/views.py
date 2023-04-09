from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Animal
from django.shortcuts import render, redirect
from inicio.forms import CracionAnimalFormulario, BuscarAnimal

def mi_vista(request):
    # return HttpResponse('<h1>Mi primera vista</h1>')
    return render(request, 'index.html')

#versión con httpresponse.
# def mostrar_fecha(request):
#     dt = datetime.now()
#     dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
#     return HttpResponse(f'<p>{dt_formateado}</p>')

def saludar(request, nombre, apellido):
    return HttpResponse(f'<h1>Hola {nombre} {apellido}</h1>') 

def mi_primer_template(request):
    archivo = open(r'C:\Users\Lautaro\Desktop\Python\Proyectos\proyecto-django\templates\mi_primer_template.html', 'r')
    # archivo = open(r'mi_primer_template.html', 'r')
    template = Template(archivo.read())
    
    archivo.close()
    
    contexto = Context()
    #es la información que le puedo pasar al template
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

#version con templates
def mostrar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    # archivo = open(r'C:\Users\Lautaro\Desktop\Python\Proyectos\proyecto-django\templates\mostrar_fecha.html', 'r')
    # archivo = open(r'mostrar_fecha.html', 'r')
    # template = Template(archivo.read())
    # archivo.close()
    template = loader.get_template(r'mostrar_fecha.html')
    
    # contexto = Context({'fecha': dt_formateado})
    # template_renderizado = template.render(contexto)
    datos = {'fecha': dt_formateado}
    #esta linea seguiria siendo el contexto
    #en el HTML le paso la llave, o sea fecha entre {{fecha}}
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)

def prueba_template(request):
    
    datos = {
        'nombre': 'Pepito',
        'apellido': 'Grillo',
        'edad': 25,
        'anios': [
            1995, 2004, 2014, 2017, 2021, 2022
        ]
    }
    
    template = loader.get_template(r'prueba_template.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)

#v1
# def crear_animal(request):
#     animal = Animal(nombre='Ricardito', edad=3)
#     print(animal.nombre)
#     print(animal.edad)
#     animal.save()
#     #ver limitaciones para que no se pueda crear con el mismo nombre
#     datos = {'animal': animal}
    
#     template = loader.get_template(r'crear_animal.html')
#     template_renderizado = template.render(datos)
#     return HttpResponse(template_renderizado)

#v2
# def crear_animal(request):
#     # print(type(request))
#     # print(type(request.POST))
#     # print(request.POST)
#     if request.method == "POST":
#         animal = Animal(nombre=request.POST['nombre'], edad=request.POST['edad'])
#         animal.save()
#     return render(request, r'crear_animal_v2.html')

#v3
def crear_animal(request):
    if request.method == "POST":
        formulario = CracionAnimalFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos= formulario.cleaned_data
            
            animal = Animal(nombre=request.POST['nombre'], edad=request.POST['edad'])
            animal.save()
            
            return redirect(r'inicio:listar_animales')
    
    formulario = CracionAnimalFormulario()
    return render(request, r'crear_animal_v3.html', {'formulario': formulario})

def lista_animales(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    if nombre_a_buscar:
        # animales = Animal.objects.filter(nombre = nombre_a_buscar)
        animales = Animal.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        animales = Animal.objects.all()
    # print(animales)
    formulario_busqueda = BuscarAnimal()
    return render(request, r'lista_animales.html', {'animales': animales,'formulario': formulario_busqueda})

def prueba_render(request):
    datos = {'nombre': 'Pepe'}
    return render(request, r'prueba_render.html', datos)