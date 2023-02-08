from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from coaches.models import *
from django.views.generic import CreateView, DeleteView, UpdateView


@login_required
def controlpanel(request):
    coaches = Coaches.objects.all()
    context = {
        'coaches':coaches,
    }
    return render(request, 'coaches/controlpanel_coaches.html', context=context)

class CoachesCreateView(CreateView):
    model = Coaches
    template_name = 'coaches/add_coaches.html'
    fields = '__all__'
    success_url = '/coaches/controlpanel-coaches/'

def list_coaches(request):
    if 'search' in request.GET:
        search = request.GET['search']
        coaches = Coaches.objects.filter(title__contains=search)
    else:
        coaches = Coaches.objects.all()
    context = {
        'coaches':coaches,
    }
    return render(request, 'coaches/list_coaches.html', context=context)

class CoachesUpdateView(UpdateView):
    model = Coaches
    template_name = 'coaches/edit_coaches.html'
    fields = '__all__'
    success_url = '/coaches/controlpanel-coaches/'


class CoachesDeleteView(DeleteView):
    model = Coaches
    template_name_suffix = '_confirm_delete'
    success_url = '/coaches/controlpanel-coaches/'