from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from product_account.models import *
from django.views.generic import CreateView, DeleteView, UpdateView


@login_required
def controlpanel(request):
    product_account = Product_account.objects.all()
    context = {
        'product_account':product_account,
    }
    return render(request, 'product_account/controlpanel_product_account.html', context=context)

class Product_accountCreateView(CreateView):
    model = Product_account
    template_name = 'product_account/add_product_account.html'
    fields = '__all__'
    success_url = '/product_account/controlpanel-product_account/'

def list_product_account(request):
    if 'search' in request.GET:
        search = request.GET['search']
        product_account = Product_account.objects.filter(title__contains=search)
    else:
        product_account = Product_account.objects.all()
    context = {
        'product_account':product_account,
    }
    return render(request, 'product_account/list_product_account.html', context=context)

class Product_accountUpdateView(UpdateView):
    model = Product_account
    template_name = 'product_account/edit_product_account.html'
    fields = '__all__'
    success_url = '/product_account/controlpanel-product_account/'


class Product_accountDeleteView(DeleteView):
    model = Product_account
    template_name_suffix = '_confirm_delete'
    success_url = '/product_account/controlpanel-product_account/'