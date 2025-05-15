from django.urls import path
from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct,\
      deleteproduct, confirmdeleteproduct, edit_product_get, edit_product_post

urlpatterns = [
    path('', landingview),

    # Product url's
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),

    # Supplier url's
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
]
