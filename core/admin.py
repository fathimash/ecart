from django.contrib import admin
from core import models

admin.site.register(models.FeedbackModel)
admin.site.register(models.ProductModel)
admin.site.register(models.CategoryModel)
admin.site.register(models.UnitModel)
admin.site.register(models.CartModel)
admin.site.register(models.CartItemModel)
