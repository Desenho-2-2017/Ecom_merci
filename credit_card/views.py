from django.shortcuts import render
from django.views.generic.edit import FormView

class CreditCardDetailView(FormView):
    """ Class for CreditCard registration view."""

    http_method_names = [u'get', u'post']

    def get(self, request):
        form = CreditCardRegisterForm()
        response = render(request, 'credit_card.html', {'form': form})
        return response

    def post(self, request):
        form = CreditCardRegisterForm(request.POST)
        response = render(request, 'credit_card.html', {'form': form})
        return response

# class CreditCard(View):
#     pass


# Cadastrar dados do cartão
# Forma de pagamento

#add
#isValidCard tipo CreditCard
#
#
