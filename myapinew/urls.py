from django.urls import include,path
from rest_framework import routers
from . import views 

# routing the database to the respective url
router = routers.DefaultRouter()
router.register(r'res_sale_model', views.resSaleViewSet)
router.register(r'res_rent_model', views.resRentViewSet)
router.register(r'res_pg_model', views.resPgViewSet)
router.register(r'comm_sale_model', views.commSaleViewSet)
router.register(r'comm_lease_model', views.commLeaseViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]