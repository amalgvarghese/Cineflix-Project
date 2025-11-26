from django.urls import path

from . import views

urlpatterns = [

    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('add-phone/',views.AddPhoneView.as_view(),name='add-phone'),
    path('verify-otp/',views.VerifyOTPView.as_view(),name='verify-otp'),
]