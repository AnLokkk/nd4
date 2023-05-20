from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Product
from .filters import ProductFilter
from django.http import HttpResponse


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def qet_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['time_now'] = datetime.utcnow()
        contex['next_sale'] = "Распродажа уже сегодня!"
        contex['filterset'] = self.filterset
        return contex


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

#
# def multiply(request):
#     number = request.GET.get('number')
#     multiplier = request.GET.get('multiplier')
#
#     try:
#         result = int(number) * int(multiplier)
#         html = f'<html><body>{number}*{multiplier}={result}</body></html>'
#     except (ValueError, TypeError):
#         html = f'<html><body>Invalid input.</body></html>'
#
#     return HttpResponse(html)