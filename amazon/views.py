from django.shortcuts import render

# Create your views here.
def ipad(request):
    p={'model': 'Ipad Air (2023)', 'cost':'60,000'}
    return render(request,'ipad.html',p)

def mitab(request):
    q={'model': 'Mi Tab', 'cost':'25,000'}
    return render(request,'mitab.html',q)