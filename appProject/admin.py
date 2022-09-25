from django.contrib import admin
from .models import product_sneakers, product_t_shirt, product_hat, product_pant, product_football_sneakers

admin.site.register(product_sneakers)
admin.site.register(product_t_shirt)
admin.site.register(product_hat)
admin.site.register(product_pant)
admin.site.register(product_football_sneakers)
