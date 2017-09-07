from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from users.forms import CustomerUserRegistrationForm
from users.models import CustomerUser


class CustomerUserRegistrationView(FormView):
    """
    Class for CustomerUser registration view.
    """
    http_method_names = [u'get', u'post']

    def get(self, request):
        form = CustomerUserRegistrationForm()
        response = render(request, 'signup.html', {'form': form}) # This template name probably will change
        return response

    def post(self, request):
        form = CustomerUserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.save()
            # login(request, user)
            # response = render(request, 'homepage.html') # This template name probably will change
            response = redirect('/') # Just for now
        else:
            response = render(request, 'signup.html', {'form': form}) # This template name probably will change

        return response
