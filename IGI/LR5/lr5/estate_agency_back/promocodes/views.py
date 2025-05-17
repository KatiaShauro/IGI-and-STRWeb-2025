from django.shortcuts import render

from .models import Promocode


# Create your views here.
def promocodes(request):
    proms = Promocode.objects.order_by('-available_period')[:10]
    return render(request, "promocodes/promocodes.html",
                  {"promocodes": proms})