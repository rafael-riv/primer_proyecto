from primer_proyecto import ninja_gold
from django.http.response import HttpResponse
from django.shortcuts import redirect, render 
from django.utils.crypto import get_random_string
from random import randint

def index(request):
    return render(request,"ninja_gold.html")

def proces_money(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
    gold = 0
    if request.POST['place'] == 'farm':
        gold = randint(10,20)

    elif request.POST['place'] == 'cave':
        gold = randint(5,10)

    elif request.POST['place'] == 'house':
        gold = randint(2,5)
    else:
        gold = randint(-50,50)

    request.session['gold'] += gold
    request.session['activities'].append(f"Ganaste {gold} en  {request.POST['place']}")
    request.session.save()

    return redirect("/ninja/home")


