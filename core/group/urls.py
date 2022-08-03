from rest_framework.routers import SimpleRouter

from group.views import GroupViewset

router = SimpleRouter()
router.register("groups", GroupViewset)

urlpatterns = router.urls
