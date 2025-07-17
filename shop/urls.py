from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_form'),
    path('stock/', views.stock_management, name='stock_management'),
    path('sales/invoice/', views.sales_invoice, name='sales_invoice'),
    path('customers/ledger/', views.customer_ledger, name='customer_ledger'),
    path('suppliers/ledger/', views.supplier_ledger, name='supplier_ledger'),
    path('expenses/', views.expense_record, name='expense_record'),
    path('reports/profit-loss/', views.profit_loss_report, name='profit_loss_report'),
    path('', views.login_view, name='shop-login'),
    path('logout/', views.user_logout, name='logout'),

    # path('backup/', views.backup, name='backup'),
]