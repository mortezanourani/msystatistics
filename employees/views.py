from django.db.models import Model
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import generic

from .models import Employee

class IndexView(generic.ListView):
    template_name = "employees/index.html"
    context_object_name = "employees_list"

    def get_queryset(self):
        return Employee.objects.order_by("last_name")[:10]

class DetailView(generic.DetailView):
    model = Employee
    template_name = "employees/detail.html"

def update(request, employee_id):
    return HttpResponse(request.POST["seen_code"])
