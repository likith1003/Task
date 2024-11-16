from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    EUFO = UserForm()
    EIFO = InfoForm()
    d = {'EUFO': EUFO, 'EIFO': EIFO}
    if request.method == 'POST':
        UFDO = UserForm(request.POST)
        IFDO = InfoForm(request.POST)
        if UFDO.is_valid() and IFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.username = UFDO.cleaned_data.get('email')
            MUFDO.set_password(pw)
            MPFDO = IFDO.save(commit=False)
            MPFDO.username = MUFDO
            role = IFDO.cleaned_data.get('Role')
            if role in ('Owner', 'Director'):
                MUFDO.is_staff=True
                MUFDO.is_superuser=True
            MUFDO.save()
            MPFDO.save()
            return HttpResponse('User Registration Is successfull')
        return HttpResponse('Invaalid data')
    return render(request, 'register.html', d)

def login(request):
    return render(request, 'login.html')
