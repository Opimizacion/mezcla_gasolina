from django.urls import path, include
from rest_framework import routers
from optimizacion import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('producto', views.producto.ProductoList.as_view(),name='Lista de productos intermedios'),
    path('producto/<int:pk>', views.producto.ProductoDetail.as_view(),name='Crud de productos intermedios'),
    path('producto_mezcla', views.producto.MezclaProducto.productoReformador,name='Mezcla de productos intermedios al reformador'),
    path('modelo', views.producto.MezclaProducto.detallesResultantes,name='Resultados del modelo'),

    path('restriccion', views.restriccion_producto.RestriccionList.as_view(),name='Lista de restricciones de los productos finales'),
    path('restriccion/<int:pk>', views.restriccion_producto.RestriccionDetail.as_view(),name='Crud de restricciones de los productos finales'),

    path('producto_final', views.producto_final.ProductoFinalList.as_view(),name='Lista de productos finales'),
    path('producto_final/<int:pk>', views.producto_final.ProductoFinalDetail.as_view(),name='Crud de los productos finales'),

]