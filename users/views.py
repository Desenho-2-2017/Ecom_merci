from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from .models import CustomerUser
from users.forms import CustomerUserRegistrationForm, CustomerUserDelectionForm
from users.forms import CustomerUserUpdateForm
from django.contrib.auth import authenticate
from django.contrib import messages


# data = {}


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
            user = form.save()
            user.save()
            # login(request, user)
            # This template name below probably will change
            # response = render(request, 'homepage.html')
            response = redirect('/')  # Just for now
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
                # response = render_mensagem_erro(request, 'Senha incorreta!\
                #     Digite novamente.', 'excluirConta.html', {'data': data})

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
        instance = CustomerUser.objects.get(id=id)
        form = CustomerUserUpdateForm(request.POST or None, instance=instance)

        # Temporary template, should redirect to sucess page in the future
        if form.is_valid():
            form.save()
            return redirect('/')

        response = render(request, 'edit.html', {'form': form})

        return response
