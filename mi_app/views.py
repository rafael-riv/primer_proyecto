from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, localtime, strftime

# Create your views here.
def index(request):

    return HttpResponse("Hola esta es mi respuesta")

def index(request):# no se pasan valores a través de URL
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")   

def new(request):       # no se pasan valores a través de URL
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")                         
    
def show(request, number):# no se pasan valores a través de URL
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}") 

def edit(request, number):# no se pasan valores a través de URL
    return HttpResponse(f"placeholder para editar el blog {number} llamado 'edit'")                          # dado el ejemplo anterior, my_val sería 23
    
def root(request):
	return redirect("/blogs")

def create(request):
	return redirect("/")

def destroy(request,number):
	return redirect("/blogs")

def json(request):
    return JsonResponse({
        "Nombre" : "Juan"
    })

def home(request):
    context = {
        'imagenes' : ['https://kaikucaffelatte.com/blog/wp-content/uploads/2020/03/shutterstock_510679489-scaled.jpg',
        'https://astelus.com/wp-content/viajes/Lago-Moraine-Parque-Nacional-Banff-Alberta-Canada.jpg',
        'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg',
        'https://www.nationalgeographic.com.es/medio/2018/02/27/playa-de-isuntza-lekeitio__1280x720.jpg'],

        'time' : strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request,'index.html', context)







