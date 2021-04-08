from django.urls import path, include
from . import views


urlpatterns = [
    path('products/', include('apps.products.urls'))
]
