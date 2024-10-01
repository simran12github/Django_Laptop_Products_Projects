from .views import type_req, ProductView, ProfileDetailView
from django.urls import path

urlpatterns = [
    path("crud", type_req),
    path("prodhtml",ProductView.as_view(), name = "product_list"),
    path("profhtml/<int:pk>",ProfileDetailView.as_view(), name = "profile_detail"),

]
