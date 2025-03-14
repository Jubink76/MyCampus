from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request,'home.html')
#########################################################################################################################################

def student_register(request):
    return render(request,'student_reg.html')

#########################################################################################################################################

