from django.urls import path, include

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/optimizacion/', include('optimizacion.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]