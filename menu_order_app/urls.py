from django.urls import path
from django.contrib.auth import views as auth_views
from menu_order_app import views

app_name = 'menu_order_app'

urlpatterns = [
    # path('Members/',views.members_recode.as_view(),name='members')
    path('add_dish/',views.add_dish,name='add_dish'),
    path('menu_dish',views.menu_dish,name='menu_dish'),
    path('registration/',views.order_register_view,name='register'),
    path("login/",auth_views.LoginView.as_view(template_name='menu_order_app/login.html'),name='login'),
    path("logout/",auth_views.LogoutView.as_view(template_name='menu_order_app/logout.html'),name='logout'),
    path("signup/",views.SingUp,name='signup'),
    # path('order_item',views.order_item_view,name='order_item')
]
