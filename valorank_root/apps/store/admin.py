from django.contrib import admin
from .models import BaseRank, DesiredRank, Product

admin.site.register(BaseRank)
admin.site.register(DesiredRank)
admin.site.register(Product)
