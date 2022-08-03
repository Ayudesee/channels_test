from rest_framework.routers import SimpleRouter

from tack.views import TackViewset

router = SimpleRouter()
router.register("tacks", TackViewset)

urlpatterns = router.urls
