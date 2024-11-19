from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic

from .models import Gym

# Create your views here.
class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "gyms_list"

    def get_queryset(self):
        return Gym.objects.order_by("-issuance_date")[:5]

class DetailView(generic.DetailView):
    model = Gym
    template_name = "detail.html"
