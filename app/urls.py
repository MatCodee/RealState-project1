from django.urls import path
from .views import (
    home_page,
    nosotros_page,
    servicios_page,
    contacto_page,
    arriendo_page,
    venta_page,
    detail_service,
    HomeView,
    TestView,
    HomeViewRequest,
)


urlpatterns = [
    path('',HomeViewRequest.as_view()),
    path('home/',HomeView.as_view()),
    path('contacto/',contacto_page,name = 'contacto'),
    path('nosotros/',nosotros_page,name = 'nosotros'),
    path('servicios/',servicios_page,name = 'servicios'),
    
    path('<int:id>/',detail_service, name = 'detail'),
    # funciones de venta y arriendo
    path('venta/',venta_page,name = 'venta'),
    path('arriendo/',arriendo_page,name = 'arriendo'),
]
