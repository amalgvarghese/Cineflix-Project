from django.urls import path

from . import views
urlpatterns=[

    path('razorpay/<str:uuid>/',views.RazorPayView.as_view(),name='razorpay'),
]

    