from django.urls import path

from catalog.views import ContactView, ProductDetailView, ProductListView

app_name = "catalog"


urlpatterns = [
    path("contacts/", ContactView.as_view(), name="contact"),
    path("home/", ProductListView.as_view(), name="home"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
