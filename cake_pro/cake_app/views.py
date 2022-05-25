from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from .forms import customerForm, UserForm, AddcakeForm
from .models import cake, customer, orderplaced, payment


def index(request):
    return render(request, 'index.html')


def admhome(request):
    return render(request, 'adm/index.html')


def login(request):
    return render(request, 'registration/login.html')


def userview(request):
    user = request.user
    if user.is_staff:
        return redirect('admhome')
    elif user.is_customer:
        return redirect('cxhome')
    elif user.is_maker:
        return redirect('makerhome')
    else:
        return redirect('index')


def cxhome(request):
    return render(request, 'customer/index.html')


def makerhome(request):
    return render(request, 'cake_maker/index.html')


def signup(request):
    form = UserForm
    n_form = customerForm()
    if request.method == 'POST':
        form = UserForm(request.POST, )
        n_form = customerForm(request.POST, )
        if form.is_valid() and n_form.is_valid():
            user = form.save(commit=False)
            user.is_customer = True
            user.save()
            s = n_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'Add Successfully')
            return redirect('signup')
    return render(request, 'register.html', {'form': form, 'n_form': n_form})


def signup1(request):
    form = UserForm
    n_form = customerForm()
    if request.method == 'POST':
        form = UserForm(request.POST, )
        n_form = customerForm(request.POST, )
        if form.is_valid() and n_form.is_valid():
            user = form.save(commit=False)
            user.is_maker = True
            user.save()
            s = n_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'Add Successfully')
            return redirect('signup1')
    return render(request, 'register1.html', {'form': form, 'n_form': n_form})


def add_cake(request):
    form = AddcakeForm()

    if request.method == 'POST':
        form = AddcakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'cakeAdd Successfully')
            return redirect('add_cake')
    return render(request, 'cake_maker/add_cake.html', {'form': form})


def viewcake(request):
    dataset = cake.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'cake_maker/viewcake.html', context)

def viewcakess(request):
    dataset = cake.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'cake_maker/viewcakess.html', context)

def view_customers(request):
    dataset = customer.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'adm/view_customer.html', context)

def view_maker(request):
    dataset = customer.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'adm/view_maker.html', context)

def update_customer(request, id=None):
    data = customer.objects.get(id=id)
    form = customerForm(instance=data)
    if request.method == 'POST':
        form = customerForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.info(request, ' updated Successfully')
            return redirect('view_customers')

    return render(request, 'adm/update_customer.html', {'form': form})



def update_cake(request, id=None):
    data = cake.objects.get(id=id)
    form = AddcakeForm(instance=data)
    if request.method == 'POST':
        form = AddcakeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.info(request, ' updated Successfully')
            return redirect('viewcake')

    return render(request, 'cake_maker/update_cake.html', {'form': form})


def delete_cake(request, id=None):
    data = cake.objects.get(id=id)
    data.delete()
    return redirect('view_cake')


def add_order(request, id=None):
    u = customer.objects.get(user=request.user)
    accessory = cake.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        category = request.POST.get('category')
        description = request.POST.get('description')
        ob = orderplaced()
        ob.title = title
        ob.price = price
        ob.category = category
        ob.description = description
        ob.customer = u
        ob.save()
        messages.info(request, 'Requested')
        return redirect('view_order')

    return render(request, 'customer/add_order.html', {'key': accessory})


def view_cake(request):
    dataset = cake.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'customer/view_cake.html', context)


def view_order(request):
    dataset = orderplaced.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'customer/view_order.html', context)


def view_cake_order(request):
    dataset = orderplaced.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'cake_maker/view_cake_order.html', context)

def confirm_order(request, id):
    req = orderplaced.objects.get(id=id)
    req.order_status = 1

    req.save()

    messages.info(request, 'Approved  Application')
    return redirect('view_cake_order')


def rej_order(request, id):
    req = orderplaced.objects.get(id=id)
    req.order_status = 2
    req.save()
    return redirect('view_cake_order')


def delete_order(request, id=None):
    data = orderplaced.objects.get(id=id)
    data.delete()
    return redirect('view_order')


def payments(request, id):
    u = customer.objects.get(user=request.user)
    accessory = orderplaced.objects.get(id=id)
    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address')
        price = request.POST.get('price')
        card_number = request.POST.get('card_number')
        cvv = request.POST.get('cvv')
        date = request.POST.get('date')

        ob = payment()

        ob.shipping_address = shipping_address
        ob.price = price
        ob.card_number = card_number
        ob.cvv = cvv
        ob.date = date
        ob.custom = u

        ob.save()
        messages.info(request, 'orderplaced successfully')
        return redirect('cxhome')

    return render(request, 'customer/payment.html', {'key': accessory})

def view_adm_cake(request):
    dataset = cake.objects.all()
    context = {
        'data': dataset
    }
    return render(request,'cake_maker/view_adm_cake.html', context)