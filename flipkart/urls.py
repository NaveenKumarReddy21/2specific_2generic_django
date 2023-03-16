from django.urls import path
from flipkart.views import *

app_name='flipkart'

urlpatterns=[
    path('samsungtab/',samsungtab,name='samsungtab'),
    path('realmetab/',realmetab,name='realmetab'),
    
]