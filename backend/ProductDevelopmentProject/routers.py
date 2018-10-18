from rest_framework.routers import SimpleRouter
from risks.views import RiskTypeViewSet, FieldViewSet
from risks.views import RiskViewSet, FieldRiskViewSet
router = SimpleRouter()
router.register("field", FieldViewSet)
router.register("risktype", RiskTypeViewSet)
router.register("risk", RiskViewSet)
router.register("fieldrisk", FieldRiskViewSet)

urlpatterns = router.urls
