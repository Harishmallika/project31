from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *





def djforms(request):
    ENFO=nameform()
    d={'ENFO':ENFO}

    if request.method=='POST':
        NFDO=nameform(request.POST)
        if NFDO.is_valid():
            return HttpResponse(str(NFDO.cleaned_data))
            
        else:
            return HttpResponse('data is not valid')     


        





    
    return render(request,'djforms.html',d)
