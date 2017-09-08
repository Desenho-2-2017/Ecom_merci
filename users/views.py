from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from users.forms import CustomerUserRegistrationForm


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
