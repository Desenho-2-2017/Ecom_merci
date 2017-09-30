from .models import CustomerUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, UpdateView
from users.forms import (
    CustomerUserDelectionForm,
    CustomerUserRegistrationForm,
    CustomerUserUpdateForm,
    LoginForm)


class CustomerUserRegistrationView(FormView):

    """
    Class for CustomerUser registration view.
    """
    http_method_names = [u'get', u'post']

    def get(self, request):
        form = CustomerUserRegistrationForm()
        # This template name below probably will change
        response = render(request, 'signup.html', {'form': form})
        return response

    def post(self, request):
        form = CustomerUserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # This template name below probably will change
            response = redirect("/")
        else:
            # This template name below probably will change
            response = render(request, 'signup.html', {'form': form})

        return response


class CustomerUserDelectionView(FormView):

    http_method_names = [u'get', u'post']

    def get(self, request):
        form = CustomerUserDelectionForm()
        response = render(request, 'excluirConta.html', {'form': form})
        return response

    def post(self, request):
        form = CustomerUserDelectionForm(request.POST)

        if form.is_valid():
            data = {}
            data['password'] = request.POST['password']

            password = request.POST['password']

            # utilizando o authenticate do django
            user = authenticate(username=request.user.username,
                                password=password)
            if user is not None:
                user = form.delete()
                user.delete()
                messages.sucess(request, 'Sua conta foi excluída')
                response = render(request, 'signup.html')
                return response
            else:
                pass

        else:
            response = render(request, 'excluirConta.html', {'form': form})

        return response


class CustomerUserUpdateView(UpdateView):
    """
    Class for CustomerUser edit/update view implementation
    """

    model = CustomerUser
    slug_field = 'id'
    pk_url_kwarg = 'id'
    fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def get_queryset(self):
        return CustomerUser.objects.all()

    def get(self, request, id):
        if request.user.id == int(id):
            instance = CustomerUser.objects.get(id=id)
            form = CustomerUserUpdateForm(request.POST or None,
                                          instance=instance)

            # Temporary template, should redirect to sucess page in the future
            if form.is_valid():
                form.save()
                return redirect('/')

            response = render(request, 'edit.html', {'form': form})
        else:
            response = redirect('/')

        return response


class CustomerUserDetailView(DetailView):
    model = CustomerUser

    def get_context_data(self, **kwargs):

        if self.request.user.id == kwargs['object'].id:
            context = super(CustomerUserDetailView,
                            self).get_context_data(**kwargs)
            context['context_object_name'] = CustomerUser._meta.verbose_name
        else:
            context = redirect('/')

        return context


class CustomerUserListView(ListView):
    model = CustomerUser

    def get_context_data(self, **kwargs):

        context = super(CustomerUserListView,
                        self).get_context_data(**kwargs)
        context['context_object_name'] = CustomerUser._meta.verbose_name
        context['context_object_name_plural'] = (
            CustomerUser._meta.verbose_name_plural)
        return context


class LoginView(FormView):
    """
    Class for CustomerUser login view.
    """
    http_method_names = [u'get', u'post']

    def get(self, request):
        if not request.user.is_authenticated:
            form = LoginForm()
            response = render(request, 'login.html', {'form': form})
        else:
            response = redirect('/')

        return response

    def post(self, request):
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = redirect('/')
        else:
            messages.error(request, 'Nome de usuário e/ou senha incorreto(s).')
            response = render(request, 'login.html', {'form': form})

        return response


class LogoutView(FormView):
    """
    Class for CustomerUser logout view.
    """
    http_method_names = [u'get']

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            response = redirect('/')
        else:
            response = redirect('/')

        return response
