from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home' ),
    path('ordernow/',views.ordernow, name='ordernow' ),
    path('orders/',views.orders, name='orders' ),
    path('login',views.loginPage ,name="login"),
    path('logout',views.logoutPage ,name="logout"),
    path('register',views.userregister ,name="register"),
    path('done',views.done ,name="done"),
    path('lawyers',views.lawyersPage ,name="lawyers"),
    path('lawyerprofile/<str:pk>/',views.lawyerProfile ,name="lawyerprofile"),
    path('smsverify',views.smsverify ,name="smsverify"),
    path('addlawyer',views.addLawyer ,name="addlawyer"),
    path('order/<str:pn>/',views.order ,name="order"),
    path('editprofile',views.editprofile ,name="editprofile"),
    path('userorders',views.userOrders ,name="userorders"),
    path('social',views.social ,name="social"),
]
