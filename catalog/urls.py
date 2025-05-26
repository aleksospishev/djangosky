from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (ContactView, ProductCategoryView, ProductCreateView,
                           ProductDeleteView, ProductDetailView,
                           ProductListView, ProductUpdateView)

app_name = "catalog"


urlpatterns = [
    path("contacts/", ContactView.as_view(), name="contact"),
    path("home/", ProductListView.as_view(), name="home"),
    path("products/<int:pk>/", cache_page(5 * 60)(ProductDetailView.as_view()), name="product_detail"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("products/<str:category_slug>/", ProductCategoryView.as_view(), name="product_category"),
]
