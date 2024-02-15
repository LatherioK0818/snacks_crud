from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Snack

class SnackListView(ListView):
    model = Snack
    template_name = 'snacks/snack_list.html'
    context_object_name = 'snack_list'

class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snacks/snack_detail.html'

class SnackCreateView(CreateView):
    model = Snack
    template_name = 'snacks/snack_form.html'
    fields = ['title', 'purchaser', 'description']

class SnackUpdateView(UpdateView):
    model = Snack
    template_name = 'snacks/snack_form.html'
    fields = ['title', 'description']

class SnackDeleteView(DeleteView):
    model = Snack
    template_name = 'snacks/snack_confirm_delete.html'
    success_url = reverse_lazy('snack_list')
