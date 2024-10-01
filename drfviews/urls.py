from .views import ProductView, ProViewset, LapView
from django.urls import path, include
from  rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("crud", ProViewset, basename="product")
router.register("lap", LapView)

urlpatterns = [
    path("pro_post", ProductView.as_view()),
    path("pro_crud/<int:pk>", ProductView.as_view()),
    path("pro/",include(router.urls))
]
