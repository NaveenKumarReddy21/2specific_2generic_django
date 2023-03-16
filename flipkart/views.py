from django.shortcuts import render

# Create your views here.

def samsungtab(request):
    m={'model': 'SAMSUNG GALAXY TAB S7FE', 'cost':'45,000'}
    return render(request,'samsungtab.html',m)

def realmetab(request):
    q={'model': 'REALME PAD (2023)', 'cost':'17,000'}
    return render(request,'realmetab.html',q)