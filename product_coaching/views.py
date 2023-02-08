from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from product_coaching.models import *
from django.views.generic import CreateView, DeleteView, UpdateView


@login_required
def controlpanel(request):
    product_coaching = Product_coaching.objects.all()
    context = {
        'product_coaching':product_coaching,
    }
    return render(request, 'product_coaching/controlpanel_product_coaching.html', context=context)

class Product_coachingCreateView(CreateView):
    model = Product_coaching
    template_name = 'product_coaching/add_product_coaching.html'
    fields = '__all__'
    success_url = '/product_coaching/controlpanel-product_coaching/'

def list_product_coaching(request):
    if 'search' in request.GET:
        search = request.GET['search']
        product_coaching = Product_coaching.objects.filter(title__contains=search)
    else:
        product_coaching = Product_coaching.objects.all()
    context = {
        'product_coaching':product_coaching,
    }
    return render(request, 'product_coaching/list_product_coaching.html', context=context)

class Product_coachingUpdateView(UpdateView):
    model = Product_coaching
    template_name = 'product_coaching/edit_product_coaching.html'
    fields = '__all__'
    success_url = '/product_coaching/controlpanel-product_coaching/'


class Product_coachingDeleteView(DeleteView):
    model = Product_coaching
    template_name_suffix = '_confirm_delete'
    success_url = '/product_coaching/controlpanel-product_coaching/'