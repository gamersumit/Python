from rest_framework.routers import DefaultRouter 
from product.viewsets import ProductViewSet, ProductGenericViewSet

router = DefaultRouter()
router.register('product', ProductGenericViewSet,
                basename='products')
#router.register('pro', ProductViewSet, basename='pro')

print(router.urls)
urlpatterns = router.urls