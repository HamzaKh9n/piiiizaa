from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django import template
import datetime
# Create your views here.

def home(request):
    try:
        seller = sellers.objects.get(user = request.user)
        s_name = seller.name
        if request.method == 'POST':
            val = request.POST.get('search')
            obj = Pizza.objects.filter(name__contains = val )
            data = obj
            try:
                cart = Carts.objects.get(user = request.user)
                items = cart.cart_items.all().count()
            except:
                items = 0
            return render(request , "home.html" , {'pizza' : data , 'count':items , 'search':val , 'name':s_name}) 
        else:
            try:
                print('ryokai')
                data = Pizza.objects.all()
                cart = Carts.objects.get(user = request.user)
                items = cart.cart_items.all().count()
                for i in CartItems.objects.filter(cart=cart):
                    ids = Pizza.objects.filter(id = i.pizzas.id)
                    print(ids)
                    
                # pizzas = val.pizzas.objec ts.all()
                # for i in cart.cart_items.all()
                return render(request , "home.html" , {'pizza' : data , 'count':items  , 'n':'n' , 'cartitems':CartItems.objects.filter(cart=cart) , 'pizzas':Pizza ,'cart':cart, 'name':s_name})
            except:
                data = Pizza.objects.all()
                return render(request , 'home.html' , {'pizza':data, 'name':s_name}) 
    except: 
        if request.method == 'POST':
            val = request.POST.get('search')
            obj = Pizza.objects.filter(name__contains = val )
            data = obj
            try:
                cart = Carts.objects.get(user = request.user)
                items = cart.cart_items.all().count()
            except:
                items = 0
            return render(request , "home.html" , {'pizza' : data , 'count':items , 'search':val}) 
        else:
            try:
                print('ryokai')
                data = Pizza.objects.all()
                try:
                    cart = Carts.objects.get(user = request.user)
                    items = cart.cart_items.all().count()
                except:
                    items = 0
                for i in CartItems.objects.filter(cart=cart):
                    ids = Pizza.objects.filter(id = i.pizzas.id)
                    print(ids)
                    
                # pizzas = val.pizzas.objec ts.all()
                # for i in cart.cart_items.all()
                return render(request , "home.html" , {'pizza' : data , 'count':items  , 'n':'n' , 'cartitems':CartItems.objects.filter(cart=cart) , 'pizzas':Pizza ,'cart':cart})
            except:
                data = Pizza.objects.all()
                return render(request , 'home.html' , {'pizza':data}) 

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = username , email = email , password = password)
        if user is None:
            msg = "Incorrect Username or Password"
            return render(request , 'Auth/login.html' , {'msg':msg})
        else:
            login(request , user)
            return redirect('home')
    return render(request , 'Auth/login.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username , email , password)
        user.save()
        print(email , password , 'success')
        return redirect('login')
    return render(request , 'Auth/signup.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def cart(request , pizza_id):
    if request.user.is_authenticated:
        cart , _ = Carts.objects.get_or_create(user = request.user)
        cart.save()
        pizza = Pizza.objects.get(id = pizza_id)
        try:
            s = CartItems.objects.get(cart = cart , pizzas = pizza_id)
            print(s)
            return redirect('cart')
        except:
            i = CartItems.objects.create(
                cart = cart,
                pizzas = pizza
            )
            i.save()    
            return redirect('home')
    else:
        return redirect('login')

def details_cart(request , pizza_id):
    if request.user.is_authenticated:    
        cart , _ = Carts.objects.get_or_create(user = request.user)
        cart.save()
        pizza = Pizza.objects.get(id = pizza_id)
        try:
            s = CartItems.objects.get(cart = cart , pizzas = pizza_id)
            print(s)
            return redirect('cart')
        except:
            i = CartItems.objects.create(
                cart = cart,
                pizzas = pizza
            )
            i.save()    
            return redirect('cart')
    else:
        return redirect('login')

def cart_view(request):
    carts , _ = Carts.objects.get_or_create(user = request.user) 
    items = CartItems.objects.filter(cart=carts)
    x=0
    for i in items:
        p = i.pizzas.price
        qty = i.quantity
        ttl = p*qty
        x += int(ttl)

    return render(request , 'cart.html' , {'user':request.user , 'items':carts , 'total':x})
    
def bin(request , pizza_id):
    cart = Carts.objects.get(user = request.user)
    obj = CartItems.objects.filter(cart=cart , pizzas = pizza_id).delete()
    return redirect('cart')

def homebin(request , pizza_id):
    obj = CartItems.objects.filter(pizzas = pizza_id).delete()
    p_obj = Pizza.objects.get(id = pizza_id)
    p_obj.cart_btn = "logo"
    p_obj.save()
    return redirect('home')

def details(request , id):
    pizzas = Pizza.objects.get(id = id)
    cart , _ = Carts.objects.get_or_create(user = request.user)
    if request.user.is_authenticated:
        try:
            s = CartItems.objects.get(cart = cart , pizzas = id)
            print(s)
            btn = "Added to Cart"
        except:
            btn = 'Add to Cart'
    else:
        btn = 'Login'
    return render(request , 'details.html' , {'pizza':pizzas , 'btn':btn})

def plus(request , id):
    cart = Carts.objects.get(user = request.user)
    pizza = Pizza.objects.get(id=id)
    item = CartItems.objects.get(cart=cart , pizzas = pizza)
    item.quantity += 1
    item.save()
    return redirect('cart')

def minus(request , id):
    cart = Carts.objects.get(user = request.user)
    pizza = Pizza.objects.get(id=id)
    item = CartItems.objects.get(cart=cart , pizzas = pizza)
    item.quantity -= 1 
    item.save()
    return redirect('cart')

def sellerform(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            user = request.user
            email = request.POST.get('email')
            number = request.POST.get('number')
            state = request.POST.get('state')
            address = request.POST.get('address')
            city = request.POST.get('city')
            sellers.objects.create(
                name =name , 
                user = user ,
                gmail = email,
                phone = number,
                state = state, 
                address = address, 
                city = city
            )
            return redirect('home')
        return render(request , 'Sellers/sellerform.html')
    else:
        return redirect('login')

def pform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        img = request.FILES.get('image')
        ex_img = request.FILES.get('ex_img')
        category = request.POST.get('category')
        descrip = request.POST.get('description') 
        seller = sellers.objects.get(user = request.user)
        owner = seller
        Pizza.objects.create(
            name = name , 
            price = price,
            img = img,
            ex_img = ex_img,
            category = category,
            descrip =descrip , 
            owner = owner,
        )
        return redirect('s_pizzas')
    return render(request , 'Sellers/pizzaform.html')

def s_pizzas(request):
    seller = sellers.objects.get(user = request.user)
    pizzas = Pizza.objects.filter(owner = seller)
    s_name = seller.name
    return render(request , 'Sellers/pizzas.html' ,  {'pizzas':pizzas , 'name':s_name})

def orders(request):
    return render(request , 'order_details.html')

def orderspage(request):
    time = datetime.datetime.now()
    return render(request , 'order_page.html' , {'time':time})

def create_order(request , id):
    time = datetime.datetime.now()
    pizza = Pizza.objects.get(id=id)
    print(pizza , request.user)
    temp_order.objects.create(
        pizza = pizza,
        user = request.user,
    )
    return redirect('opage')

def pizza_bin(request , id):
    pizza = Pizza.objects.get(id = id)
    pizza.delete()
    return redirect('s_pizzas')