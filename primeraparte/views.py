from django.shortcuts import render
from django.template.loader import get_template

def Home(request):
    return render(request, 'primeraparte/templates/primeraparte/Página Pokemon/index.html')

    



