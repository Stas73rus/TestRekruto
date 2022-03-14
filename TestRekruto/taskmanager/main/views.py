from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def infoRekruto(request):
    name = request.GET.get('name', 'Rekruto')
    message = request.GET.get('message', 'Давай дружить!')
    start_message = request.GET.get('start_message', 'Rekruto! Давай дружить!')
    list_get_query = {
        'name': name,
        'message': message,
    }
    template = 'main/index.html'
    return render(request, template, list_get_query)
