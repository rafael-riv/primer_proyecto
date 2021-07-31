from django.http.response import HttpResponse
from django.shortcuts import redirect, render 
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return HttpResponse('que sucede?')

def random(request):
    
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1   

    context = {
        'unique_id' : get_random_string(length=32)
    }
    return render(request, 'index.html', context)
Usuarios = [
    {
        'nombre' : 'Juan',
        'password': '1234'
    },
    {
        'nombre' : 'Ignacio',
        'password' : 'elnacho'

    }
]
def login(request):
    if request.method== 'GET':
        return render(request , 'form.html')

    #primero recupero los input del formulario
    else:
        name_form = request.POST['nombre']
        pass_form = request.POST['password']
        #veerifico sis existe es usuario
        #se utiliza la funcion next para recorrer la lista
        user = next((u for u in Usuarios if u['nombre']==name_form),None)

        if user is None:
                request.session['nombre'] ='error'
                return redirect ('/ramdom/login') 

        if user['password'] != pass_form:
                request.session['nombre'] = 'error'
                return redirect ('/ramdom/login')
            
        request.session['password']= pass_form
        request.session['nombre']= name_form
        return redirect('/ramdom/claves')





4
"""
    if request.session['counter'] <= 10:
        context = {
            'random_word' : get_random_string(length=14)
        }
    else:
        context = {
            'random_word' : 'Alcanzaste 10 intentos, presiona reset'
        }
        request.session['counter'] = 10
        
    return render(request, 'rando.html', context)
"""


