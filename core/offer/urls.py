from rest_framework.routers import SimpleRouter

from offer.views import OfferViewset

router = SimpleRouter()
router.register("offers", OfferViewset)

urlpatterns = router.urls
