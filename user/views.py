from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

def home(request):
    return render(request,"user/home.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "user/signup.html"

#    def form_valid(self, form, account_activation_token=None):
#        response = super().form_valid(form)
#        # Отправляем письмо
#        current_site = get_current_site(self.request)
#        mail_subject = 'Activate your account.'
#        message = render_to_string('user/activation_email.html', {
#            'user': self.object,
#            'domain': current_site.domain,
#            'uid': urlsafe_base64_encode(force_bytes(self.object.pk)),
#           'token': account_activation_token.make_token(self.object),
#        })
#        to_email = form.cleaned_data.get('email')
#        email = EmailMessage(
#            mail_subject, message, to=[to_email]
#        )
#        email.send()
#        return response

@login_required
def index(request):
    return render(request,"user/home.html")