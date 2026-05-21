from django.shortcuts import render
from .models import Category,Product
# Create your views here.
def home(request):
    category = Category.objects.all()
    product = Product.objects.all()
    print(category)
    print(product)
    return render(request, 'home.html', {'categories': category, 'products': product})