from django.urls import path, include
from rest_framework import routers
from optimizacion import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('producto', views.producto.ProductoList.as_view(),name='Lista de productos'),
    path('producto/<int:pk>', views.producto.ProductoDetail.as_view(),name='Crud de productos'),
    path('producto_mezcla', views.producto.MezclaProducto.productoReformador,name='Mezcla de productos al reformador'),
    path('modelo', views.producto.MezclaProducto.detallesResultantes,name='Resultados del modelo'),
]