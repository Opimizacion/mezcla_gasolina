from django.urls import path, include
from rest_framework import routers
from optimizacion import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('producto', views.ProductoList.as_view(),name='Lista de productos'),
    path('<int:pk>/producto', views.ProductoDetail.as_view(),name='Crud de productos'),
]