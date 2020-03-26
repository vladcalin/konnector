from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from users.forms import LoginForm

from users.forms import RegisterForm
from users.models import User


class Home(TemplateView):
    template_name = 'users/login.html'


class Register(TemplateView):
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = RegisterForm()
        return context

    def post(self, request):
        form = RegisterForm(data=request.POST)
        if not form.is_valid():
            return render(request, self.template_name, context=self.get_context_data(form=form))
        else:
            user = User(username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'],
                        full_name=form.cleaned_data['full_name'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user=user)
            return HttpResponseRedirect(reverse('dashboard'))


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'app_base.html'


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/dashboard')
            form.add_error(None, 'Invalid username/password')
            form.add_error('username', '')
            form.add_error('password', '')
        return render(request, self.template_name, {'form': form})
