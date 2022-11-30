from django.db import models
from django.db.models import F,Q,Sum,Count,Avg
from django.contrib.auth import get_user_model


class FeedbackModel(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject}"


# Category


class CategoryModel(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


# Unit model


class UnitModel(models.Model):
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=8)
    convertion_rate = models.FloatField()
    secondary = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


# product


class ProductModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    size = models.CharField(max_length=10)
    image = models.ImageField(upload_to="product/image/", default="default/product.png")
    category = models.ManyToManyField(CategoryModel)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


USER = get_user_model()

# Cart Model
class CartModel(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    size = models.CharField(default=0, max_length=5)

    def items(self):
        cart_items = CartItemModel.objects.filter(
            cart=self,
            status=True,
        )
        return cart_items

    def total(self):
        amount = CartModel.objects.aggregate(
            amount=Sum(F("cartitemmodel__product__price") * F("cartitemmodel__quantity"))
        ).get("amount", 0)
        return amount

    def __str__(self):
        return f"{self.user}"


# Cart Item Model
class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product}({self.quantity})"
