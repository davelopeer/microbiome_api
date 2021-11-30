from django.shortcuts import render
from .models import Entry
from django.views.generic import ListView


class EntriesList(ListView):
    model = Entry
    template_name = 'index.html'
    context_object_name = 'entries'
    ordering = ['-pk']
    paginate_by = 1000
