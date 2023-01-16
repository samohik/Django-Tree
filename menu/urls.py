from django.urls import path

from menu.views import *

urlpatterns = [
    path('', TreeMenuView.as_view(), name='home'),
    path('<named_url>/', TreeDetailView.as_view(), name='detail'),
]
