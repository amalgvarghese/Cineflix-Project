from django.urls import path

from .import views
urlpatterns = [

    path('subscription-list/',views.SubscriptonView.as_view(),name='subscription-list')
]