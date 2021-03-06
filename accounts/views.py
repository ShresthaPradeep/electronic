from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from products.models import Product
from .models import Favourite, Cart, CartProduct, WaitList, UserProfile, Notification, Order
from .forms import RegistrationForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.template.loader import render_to_string

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


# class Register(generic.CreateView):
#     form_class = RegistrationForm
#     template_name = 'accounts/register.html'
#     success_url = reverse_lazy('index')

#     def form_valid(self, form):
#         view = super(Register, self).form_valid(form)
#         username, password, email = form.cleaned_data.get('username'),form.cleaned_data.get('password'),form.cleaned_data.get('email')
#         user = authenticate(username=username, password=password, email = email)
#         login(self.request, user)
#         return view


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check Username
        if User.objects.filter(username = username).exists():
            messages.error(request, 'That username already exists')
            return redirect('register')
        else:
            if User.objects.filter(email = email).exists():
                messages.error(request, 'That email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                auth.login(request, user)
                UserProfile.objects.create(
                    user = request.user,
                    username = username,
                    email = email
                )
                messages.success(request, 'Account created successfully')
                return redirect('index')
            
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    
    return redirect('index')

class ProfileView(generic.View):
    def get(self, *args, **kwargs):
        profiles = UserProfile.objects.filter(username = self.request.user)
        context = {
            'profiles': profiles
        }
        return render(self.request, 'accounts/profile.html', context)



def edit_profile(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        ship_address1 = request.POST['ship_address1']
        ship_address2 = request.POST['ship_address2']
        ship_phone = request.POST['ship_phone']
        ship_email = request.POST['ship_email']
        photo = request.FILES.get('photo', False)
    

        user_profile_qs = UserProfile.objects.filter(user = request.user)
        user = User.objects.get(username = request.user.username)
        if user:
            user.username = username
            user.email = email
            user.save()
        
        if user_profile_qs.exists():
            user_profile = user_profile_qs[0]
            user_profile.username = user.username
            user_profile.email = user.email
            if photo:
                user_profile.photo = photo
            user_profile.address = address
            user_profile.phone = phone
            user_profile.ship_address1 = ship_address1
            user_profile.ship_address2 = ship_address2
            user_profile.ship_phone = ship_phone
            user_profile.ship_email = ship_email
            user_profile.save()

    return redirect('profile')


@login_required
def add_to_cart(request, pk):
    profile = UserProfile.objects.get(user = request.user)
    cart_count = CartProduct.objects.filter(user = request.user)
    product = get_object_or_404(Product, id = pk)

    if 'number' in request.GET:
        if not request.GET['number']:
            quantity = 1
        else:
            quantity = request.GET['number']

    if 'color' in request.GET:
        color = request.GET['color']
     
    if product.available:
        cart_product, created = CartProduct.objects.get_or_create(
            product=product,
            user = request.user,
            quantity = quantity,
            color = color,
            checked_out = False,
            )
        
        carts = Cart.objects.filter(user = request.user)
        if carts.exists():
            cart = carts[0]
            cart.product.add(cart_product)
            cart.save()
            profile.cart = len(cart_count)
            profile.save()
        else:
            cart = Cart.objects.create(user=request.user)
            cart.product.add(cart_product)
            cart.save()
            profile.cart = len(cart)
            profile.save()

        return redirect('cart')
    else:
        messages.info(request, ("Product is out of stock"))
        return redirect('product_detail', pk)
        

def remove_from_cart(request):
    profile = UserProfile.objects.get(user = request.user)
    cart = CartProduct.objects.filter(user = request.user)
    if request.method=="GET":
        CartProduct.objects.filter(id=request.GET.get("id"), user=request.user).delete()
        print("Deleted")
        profile.cart = len(cart)
        profile.save()
        cart_count = profile.cart
        return JsonResponse({'cart': cart_count})


class CartView(LoginRequiredMixin, generic.View):
    def get(self, *args, **kwargs):
        cart = CartProduct.objects.filter(user = self.request.user)
        total = 0
        for product in cart:
            if not product.checked_out:
                total = product.quantity * product.product.selling_price + total
            

        context = {
            'cart_products': cart,
            'total': total
        }
        
        return render(self.request, 'accounts/cart.html', context)

def edit_cart(request):
    for key, value in request.POST.items():
        if key.startswith('q'):
            key = key.split('q_')
            k = int(key[1])
            product = get_object_or_404(CartProduct, id = k)
            if product:
                product.quantity = value
                product.save()

    return redirect('cart')

    
class WaitView(LoginRequiredMixin, generic.View):
    def get(self, *args, **kwargs):
        wait_products = WaitList.objects.filter(user = self.request.user)
        context = {
            'wait_products': wait_products,
        }
        return render(self.request, 'accounts/wait.html', context)


def add_to_wait(request, pk):
    profile = UserProfile.objects.get(user = request.user)
    wait = WaitList.objects.filter(user = request.user)
    product = get_object_or_404(Product, id = pk)
    wait_product, created = WaitList.objects.get_or_create(
        product=product,
        user = request.user,
        )
    
    profile.wait = len(wait)
    profile.save()
    return redirect('wait')


def add_to_cart_from_wait(request, pk):
    profile = UserProfile.objects.get(user = request.user)
    cart_count = CartProduct.objects.filter(user = request.user)
    product = get_object_or_404(Product, id = pk)

    if 'number' in request.GET:
        if not request.GET['number']:
            quantity = 1
        else:
            quantity = request.GET['number']

    if 'color' in request.GET:
        color = request.GET['color']

    if product.available:
        cart_product, created = CartProduct.objects.get_or_create(
            product=product,
            user = request.user,
            quantity = quantity,
            color = color,
            checked_out = False,
            )

        carts = Cart.objects.filter(user = request.user)
        if carts.exists():
            cart = carts[0]
            cart.product.add(cart_product)
            cart.save()
        else:
            cart = Cart.objects.create(user=request.user)
            cart.product.add(cart_product)
            cart.save()
        
        profile.cart = len(cart_count)
        profile.save()
        return redirect('cart')

    else:
        messages.info(request, ("Product is out of stock"))
        return redirect('wait')


def remove_from_wait(request):
    profile = UserProfile.objects.get(user = request.user)
    wait = WaitList.objects.filter(user = request.user)
    if request.method=="GET":
        print("Bye")
        print(request.GET)
        WaitList.objects.filter(id=request.GET.get("id"), user=request.user).delete()
        print("Deleted")
        profile.wait = len(wait)
        profile.save()
        wait_count = profile.wait
        return JsonResponse({'wait': wait_count})

       
class FavouriteView(generic.View):
    def get(self, *args, **kwargs):
        favourite_products = Favourite.objects.filter(user = self.request.user)
        context = {
            'favourite_products': favourite_products,
        }
        return render(self.request, 'accounts/favourites.html', context)


def add_to_favourite(request):
    
    print("Hello")
    profile = UserProfile.objects.get(user = request.user)
    favourite = Favourite.objects.filter(user = request.user)
    if request.method=="GET":
        fav = Favourite.objects.filter(product__id=request.GET.get("id"), user=request.user)
        if fav.exists():
            fav.delete()
            profile.fav = len(favourite)
            profile.save()
            fav = profile.fav
            return JsonResponse({'key': "deleted", 'fav': fav})
        else:
            product = get_object_or_404(Product, id = int(request.GET.get('id')))

            favourite_product, created = Favourite.objects.get_or_create(
                product=product,
                user = request.user,
                )
            profile.fav = len(favourite)
            profile.save()
            fav = profile.fav
            return JsonResponse({'key': "created", 'fav': fav})
    # return redirect(request.META.get('HTTP_REFERER', '/'))

def remove_from_favourite(request):
    profile = UserProfile.objects.get(user = request.user)
    fav = Favourite.objects.filter(user = request.user)
    if request.method=="GET":
        print("Bye")
        print(request.GET)
        Favourite.objects.filter(id=request.GET.get("id"), user=request.user).delete()
        print("Deleted")
        profile.fav = len(fav)
        profile.save()
        fav_count = profile.fav
        return JsonResponse({'fav': fav_count})


# def remove_from_favourite(request, pk):
#     product = get_object_or_404(Favourite, id=pk)
#     product.delete()
        
#     return redirect('favourite')


def add_to_cart_from_favourite(request, pk):
    profile = UserProfile.objects.get(user = request.user)
    cart_count = CartProduct.objects.filter(user = request.user)
    product = get_object_or_404(Product, id = pk)

    if 'number' in request.GET:
        if not request.GET['number']:
            quantity = 1
        else:
            quantity = request.GET['number']

    if 'color' in request.GET:
        color = request.GET['color']

    if product.available:
        cart_product, created = CartProduct.objects.get_or_create(
            product=product,
            user = request.user,
            quantity = quantity,
            color = color,
            checked_out = False,
            )

        carts = Cart.objects.filter(user = request.user)
        if carts.exists():
            cart = carts[0]
            cart.product.add(cart_product)
            cart.save()
        else:
            cart = Cart.objects.create(user=request.user)
            cart.product.add(cart_product)
            cart.save()
        profile.cart = len(cart_count)
        profile.save()
        return redirect('favourite')
    else:
        messages.info(request, (" Product is not available!! "))
        return redirect('favourite')


class NotificationView(generic.View):
    def get(self, *args, **kwargs):
        notifications = Notification.objects.filter(user = self.request.user)
        context = {
            'notifications': notifications,
        }
        return render(self.request, 'accounts/notifications.html', context)


class OrderView(generic.View):
    def get(self, *args, **kwargs):
        order_products = CartProduct.objects.filter(user = self.request.user)
        cart = get_object_or_404(Cart, user = self.request.user)

        total = 0
        for product in order_products:
            if not product.checked_out:
                total = product.quantity * product.product.selling_price + total

        context = {
            'order_products': order_products,
            'total': total,
            'cart': cart
        }
        return render(self.request, 'accounts/order.html', context)


def add_to_order(request, pk):
    cart = get_object_or_404(Cart, id = pk)

    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_address = request.POST['email_address']
        phone = request.POST['phone']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        notes = request.POST['notes']
        order = Order.objects.get_or_create(
            user = request.user,
            first_name = first_name,
            last_name = last_name,
            email = email_address,
            phone = phone,
            address = address1,
            building = address2,
            order_notes = notes,
            cart = cart,
            )
        cart.save()

        cart_products = CartProduct.objects.filter(user = request.user)
        for cart_product in cart_products:
            cart_product.checked_out = True
            cart_product.save()
    return redirect('index')
