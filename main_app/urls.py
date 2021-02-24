from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('send_mail/', SendMailView.as_view(), name='send_mail'),
    path('<slug:slug>/', Product.as_view(), name='product'),
]
