from django.db.models import Q
from django.shortcuts import render
from ecommerceapp.models import  Product


# Create your views here.

def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request,'search.html',{'query':query,'products':products})


