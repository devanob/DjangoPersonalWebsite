from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .forms import CustomAuthenticationForm
from .forms import SignupForm 
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token 
from .tasks import sendActivationEmail
from django.views.generic import View
from django.contrib.sites.shortcuts import get_current_site
import logging 
log = logging.getLogger(__name__)
# Create your views here.

class CustomLogInView(LoginView):
    authentication_form = CustomAuthenticationForm
    form_class = CustomAuthenticationForm
    template_name = 'ProjectUser/login.html'
    success_url = "home"
    redirect_authenticated_user = "home"

class CustomLogOutView(LogoutView):
    template_name = "ProjectUser/login.html"
    next_page = "home"


class CustomSignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'ProjectUser/signup.html'
    def form_valid(self, form):
        self.object = form.save()
        print(form.cleaned_data["email"])
        context = {"user_email": form.cleaned_data["email"]}
        sign_up_data = form.cleaned_data
        log.info("User Created : {}",format(sign_up_data['username']))
        log.info(type(get_current_site(self.request)))
        sign_up_data["domain"] = get_current_site(self.request).domain
        sendActivationEmail.delay(sign_up_data)
        return render(self.request, "ProjectUser/SignUpSuccess.html", 
               context)
# get current user model

User = get_user_model()
class ActivateAccount(View):
    success_url = "login"
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user.is_active ==True:
            return HttpResponse('Account Already Activated ')
        else:
            if user is not None and account_activation_token.check_token(user, token):
                # activate user and login:
                user.is_active = True
                user.save()
                login(request, user, 
                backend='ProjectUser.CustomAuthenicationBackEnd.EmailOrUsernameModelBackend')
                return HttpResponse('Account Activated')
            else:
                return HttpResponse('Activation link is invalid!')

    def post(self, request):
        pass
        # form = PasswordChangeForm(request.user, request.POST)
        # if form.is_valid():
        #     user = form.save()
        #     update_session_auth_hash(request, user) # Important, to update the session with the new password
        #     return HttpResponse('Password changed successfully')