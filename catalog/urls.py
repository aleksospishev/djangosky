from django.urls import path

from catalog.views import contacts, home, product_detail

app_name = "catalog"


urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products/<int:product_id>/", product_detail, name="product_detail"),
]
