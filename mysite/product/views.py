from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import CustomerRegistrationForm, CustomerProfileForm, MyPasswordChangeForm, SearchForm
from .models import Product, Cart, Customer, OrderPlaced
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class HomeView(View):
    def get(self, request):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam =len(Cart.objects.filter(user=request.user))

        shart = Product.objects.filter(category='T')
        m_jeans = Product.objects.filter(category='J')
        m_shoes = Product.objects.filter(category='MS')
        top = Product.objects.filter(category='TW')
        bottom = Product.objects.filter(category='BW')
        bra = Product.objects.filter(category='B')
        l_shoes = Product.objects.filter(category='LS')
        return render(request, 'product/home.html',
                      {'shart': shart, 'm_jeans': m_jeans, 'bottom': bottom, 'l_shoes': l_shoes, 'm_shoes': m_shoes,
                       'top': top, 'bra': bra, 'total_iteam':total_iteam })


class ProductDetailView(View):
    def get(self, request, id):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        product = Product.objects.get(pk=id)
        product_already_in_cart = False
        if request.user.is_authenticated:
            product_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'product/productdetail.html',
                      {'product': product, 'product_already_in_cart': product_already_in_cart, 'total_iteam':total_iteam})



class TShartView(View):
    def get(self, request, data=None):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        if data is None:
            shart = Product.objects.filter(category='T')
        elif data == 'low':
            shart = Product.objects.filter(category='T').filter(discounted_price__lte=700)
        elif data == 'high':
            shart = Product.objects.filter(category='T').filter(discounted_price__gt=700)
        return render(request, 'product/t_shart.html', {'shart': shart, 'total_iteam':total_iteam})


class JeansView(View):
    def get(self, request, data=None):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        if data is None:
            jeans = Product.objects.filter(category='J')
        elif data == 'low':
            jeans = Product.objects.filter(category='J').filter(discounted_price__lte=1500)
        elif data == 'high':
            jeans = Product.objects.filter(category='J').filter(discounted_price__gt=1500)
        return render(request, 'product/jeans.html', {'jeans': jeans, 'total_iteam':total_iteam})


class ShoesView(View):
    def get(self, request, data=None):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        if data is None:
            shoes = Product.objects.filter(category='MS')
        elif data == 'low':
            shoes = Product.objects.filter(category='MS').filter(discounted_price__lte=2500)
        elif data == 'high':
            shoes = Product.objects.filter(category='MS').filter(discounted_price__gt=2500)
        return render(request, 'product/shoes.html', {'shoes': shoes, 'total_iteam':total_iteam})


class TOpWearView(View):
    def get(self, request, data=None):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        if data is None:
            top = Product.objects.filter(category='TW')
        elif data == 'low':
            top = Product.objects.filter(category='TW').filter(discounted_price__lte=2000)
        elif data == 'high':
            top = Product.objects.filter(category='TW').filter(discounted_price__gt=2000)
        return render(request, 'product/topwear.html', {'top': top, 'total_iteam':total_iteam})


class BottomWearView(View):
    def get(self, request, data=None):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        if data is None:
            bottom = Product.objects.filter(category='BW')
        elif data == 'low':
            bottom = Product.objects.filter(category='BW').filter(discounted_price__lte=1500)
        elif data == 'high':
            bottom = Product.objects.filter(category='BW').filter(discounted_price__gt=1500)
        return render(request, 'product/bottomwear.html', {'bottom': bottom, 'total_iteam':total_iteam})


class BraView(View):
    def get(self, request, data=None):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        if data is None:
            bra = Product.objects.filter(category='B')
        elif data == 'low':
            bra = Product.objects.filter(category='B').filter(discounted_price__lte=300)
        elif data == 'high':
            bra = Product.objects.filter(category='B').filter(discounted_price__gt=300)
        return render(request, 'product/bra.html', {'bra': bra, 'total_iteam':total_iteam})

class LShoesView(View):
    def get(self, request, data=None):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        if data is None:
            lshoes = Product.objects.filter(category='LS')
        elif data == 'low':
            lshoes = Product.objects.filter(category='LS').filter(discounted_price__lte=1000)
        elif data == 'high':
            lshoes = Product.objects.filter(category='LS').filter(discounted_price__gt=1000)
        return render(request, 'product/lshoes.html', {'lshoes': lshoes, 'total_iteam':total_iteam})



@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    def get(self, request):
        user = request.user
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        Cart(user=user, product=product).save()
        return redirect('/cart')


@method_decorator(login_required, name='dispatch')
class ShowCartView(View):
    def get(self, request):
        total_iteam = 0
        if request.user.is_authenticated:
            user = request.user
            cart = Cart.objects.filter(user=user)
            total_iteam = len(Cart.objects.filter(user=user))
            amount = 0.0
            totalamount = 0.0
            shipping = 70.0
            cart_product = [p for p in Cart.objects.all() if p.user == user]
            print(cart_product)
            if cart_product:
                for cat in cart_product:
                    tempamount = (cat.quantity * cat.product.discounted_price)
                    amount += tempamount
                    totalamount = amount + shipping
                    print(amount)
                return render(request, 'product/addtocart.html',
                              {'cart': cart, 'amount': amount, 'totalamount': totalamount, 'total_iteam':total_iteam})
            else:
                return render(request, 'product/emptycart.html', {'total_iteam':total_iteam})


@method_decorator(login_required, name='dispatch')
class PlusCartView(View):
    def get(self, request):
        if request.method == 'GET':
            prod_id = request.GET['prod_id']
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.quantity += 1
            c.save()
            amount = 0.0
            shipping = 70.0
            cart_product = [p for p in Cart.objects.all() if p.user == request.user]
            for cat in cart_product:
                temtamount = (cat.quantity * cat.product.discounted_price)
                amount += temtamount

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': amount + shipping
            }
            return JsonResponse(data)


@method_decorator(login_required, name='dispatch')
class MinusCartView(View):
    def get(self, request):
        if request.method == 'GET':
            prod_id = request.GET['prod_id']
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.quantity -= 1
            c.save()
            amount = 0.0
            shipping = 70.0
            cart_product = [p for p in Cart.objects.all() if p.user == request.user]
            for cat in cart_product:
                temtamount = (cat.quantity * cat.product.discounted_price)
                amount += temtamount

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': amount + shipping
            }
            return JsonResponse(data)

class CheckoutView(View):
    def get(self, request):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_item = Cart.objects.filter(user=user)
        amount = 0.0
        shipping = 70.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for cat in cart_product:
                temtamount = (cat.quantity * cat.product.discounted_price)
                amount += temtamount
            totalamount = amount + shipping
        return render(request, 'product/checkout.html', {'add': add, 'totalamount': totalamount, 'cart_item': cart_item, 'total_iteam':total_iteam})

class PaymentdonetView(View):
    def get(self, request):
        user = request.user
        custid = request.GET.get('custid')
        customer = Customer.objects.get(id=custid)
        cart = Cart.objects.filter(user=user)
        for c in cart:
            OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
            c.delete()
            return redirect('orders')

@method_decorator(login_required, name='dispatch')
class RemoveCartView(View):
    def get(self, request):
        if request.method == 'GET':
            prod_id = request.GET['prod_id']
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.delete()
            amount = 0.0
            shipping = 70.0
            cart_product = [p for p in Cart.objects.all() if p.user == request.user]
            for cat in cart_product:
                temtamount = (cat.quantity * cat.product.discounted_price)
                amount += temtamount

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': amount + shipping
            }
            return JsonResponse(data)


def buy_now(request):
    return render(request, 'app/buynow.html')


class CustomerProfileView(View):
    def get(self, request):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        form = CustomerProfileForm()
        return render(request, 'product/profile.html', {'form': form, 'active': 'btn-primary', 'total_iteam':total_iteam})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            village = form.cleaned_data['village']
            postcode = form.cleaned_data['postcode']
            thana = form.cleaned_data['thana']
            district = form.cleaned_data['district']
            reg = Customer(user=usr, name=name, village=village, postcode=postcode, thana=thana, district=district)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Update Successfully ')

        return redirect('/address', {'total_iteam':total_iteam})


class CustomerAddressView(View):
    def get(self, request):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        details = Customer.objects.filter(user=request.user)
        return render(request, 'product/address.html', {'add': details, 'active': 'btn-primary', 'total_iteam':total_iteam})

class OrderView(View):
    def get(self, request):
        total_iteam = 0
        if request.user.is_authenticated:
            total_iteam = len(Cart.objects.filter(user=request.user))
        p_or = OrderPlaced.objects.filter(user=request.user)
        return render(request, 'product/orders.html', {'oreder': p_or, 'total_iteam':total_iteam})



class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'product/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registration Successfully ')
            form.save()
        return render(request, 'product/customerregistration.html', {'form': form})

class SearchView(View):
    def get(self, request):
        if request.method == 'GET':
            quary = request.GET.get('quary')
            if quary:
                product = Product.objects.filter(title__icontains=quary)
                if len(product)>0:
                    return render(request, 'product/search.html', {'product':product})
                else:
                    messages.warning(request, 'This product is stock out')
                    return render(request, 'product/blanck.html')
            else:
                return redirect('/')