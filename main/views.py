from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.models import Contact

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, RegisterUserForm
from .utils import *
# Create your views here.


def index(request):
    contacts = Contact.objects.all()

    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'main/main.html', {'form':form,'contacts': contacts})


def contact_view(request):
    contacts = Contact.objects.all()
    return render(request, 'main/contacts.html', {'contacts': contacts})


class Index(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'main/main.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))