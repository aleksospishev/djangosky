from django.urls import path

from catalog.views import (
    ContactView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
)

app_name = "catalog"


urlpatterns = [
    path("contacts/", ContactView.as_view(), name="contact"),
    path("home/", ProductListView.as_view(), name="home"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),  # noqa: E501
]
