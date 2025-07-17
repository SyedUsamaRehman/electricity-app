from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense, Product, Customer, Order, Category
from .forms import ProductForm, CustomerForm, OrderForm, ExpenseForm
from django.db.models import Sum
from django.contrib.auth import authenticate

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib import messages




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'shop/login.html')
def user_logout(request):
    auth_logout(request)
    return redirect('shop-login')

@login_required
def dashboard(request):
    total_products = Product.objects.count()
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()
    total_sales = Order.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
    context = {
        'total_products': total_products,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'total_sales': total_sales,
    }
    return render(request, 'shop/dashboard.html', context)

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form})

@login_required
def stock_management(request):
    products = Product.objects.all()
    return render(request, 'shop/stock_management.html', {'products': products})

@login_required
def sales_invoice(request):
    orders = Order.objects.all()
    total_sales = orders.aggregate(Sum('quantity'))['quantity__sum'] or 0
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_invoice')
    else:
        form = OrderForm()
    return render(request, 'shop/sales_invoice.html', {'form': form, 'orders': orders, 'total_sales': total_sales})

@login_required
def customer_ledger(request):
    customers = Customer.objects.all()
    return render(request, 'shop/customer_ledger.html', {'customers': customers})

@login_required
def supplier_ledger(request):
    # Placeholder for supplier ledger functionality
    orders = Order.objects.all()
    return render(request, 'shop/supplier_ledger.html', {'order': orders})
    
@login_required
def expense_record(request):


    expense= Expense.objects.all()
    print(expense)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_record')
    else:
        form = ExpenseForm()
    return render(request, 'shop/expense_record.html', {'form': form,'expenses': expense})

@login_required
def profit_loss_report(request):
    total_income = Order.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
    total_expenses = 0  # Placeholder for total expenses calculation
    profit_loss = total_income - total_expenses
    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'profit_loss': profit_loss,
    }
    return render(request, 'shop/profit_loss_report.html', context)