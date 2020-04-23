from django.urls import path
from .views import home, HelloView

urlpatterns = [
    path('', home, name='index'),
    path('purchases/', HelloView.as_view(), name='hello'),
]
