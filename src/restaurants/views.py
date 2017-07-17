from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

import random

def home(request):
    num, num1, num2 = random.randint(0, 100000), random.randint(0, 100000), random.randint(0, 100000)
    context = {
        'context': True, 
        'num': [num, num1, num2]
    }
    return render(request, 'home.html', context)

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        num, num1, num2 = random.randint(0, 100000), random.randint(0, 100000), random.randint(0, 100000)
        context = {
            'context': True, 
            'num': [num, num1, num2]
        }
        return context