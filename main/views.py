from django.shortcuts import render,redirect
from .models import Category,Product,AddToFavorite
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    category = Category.objects.all()
    product = Product.objects.all()
    print(category)
    print(product)
    return render(request, 'home.html', {'categories': category, 'products': product}) 

def handle_login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login.html')

def handle_signup(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')


def handle_logout(request):
    logout(request)
    return redirect('home')

def view_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if not product:
        return redirect(request, '404.html')
    user = request.user.id
    is_added = AddToFavorite.objects.filter(product=product, user=user).exists()
    print(is_added)
    return render(request, 'product_page.html', {'product': product,"is_added":is_added})

def handle_add_to_favor(request,product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    AddToFavorite.objects.create(product=product, user=user)
    return redirect('view_product', product_id=product_id)

def handle_remove_from_favor(request,product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    AddToFavorite.objects.filter(product=product, user=user).delete()
    return redirect('view_product', product_id=product_id)