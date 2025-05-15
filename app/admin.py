# Jos rekisteroi tällä tavalla adminille oman appin
# modelit, voi myös admin sivuilta muokata näitä tietoja
from django.contrib import admin

from app.models import Supplier, Product

@admin.register(Product)                        # Registers your model with the admin site
class ProductAdmin(admin.ModelAdmin):           #ProductAdmin: Configures how Product appears in admin
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


# Django includes a built-in admin interface (admin.py) so developers/admins can quickly manage data without writing custom views or templates.