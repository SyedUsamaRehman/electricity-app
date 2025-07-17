from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # path('users/', views.user_list, name='user_list'),
    # path('users/add/', views.user_create, name='user_add'),
    # path('users/edit/<int:pk>/', views.user_edit, name='user_edit'),
    # path('users/delete/<int:pk>/', views.u, name='user_delete'),
]