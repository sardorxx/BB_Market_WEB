from django.core.paginator import Paginator
from django.shortcuts import render

from marketface.models import Product


# Create your views here.

def category_product(request):

    p = Paginator(Product.objects.all(), 6)
    page = request.GET.get('page')
    products1 = p.get_page(page)
    context = {
        'products1': products1
    }
    return render(request, 'marketface/home_content.html', context)
