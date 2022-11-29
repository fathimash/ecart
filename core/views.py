from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from core import models as core_models
from core.forms import FeedbackForm, ProductForm
from user import models as user_models


# home view
class HomeView(views.TemplateView):
    template_name = "core/home.html"

    extra_context = {"products": core_models.ProductModel.objects.filter(status=True)}


# about_us view
class AboutView(views.TemplateView):
    template_name = "core/about_us.html"




# ================================= FEEDBACK ================================= #


# feedback create view
class FeedbackCreateView(views.CreateView):
    template_name = "core/feedback_create.html"
    model = core_models.FeedbackModel
    form_class = FeedbackForm
    success_url = reverse_lazy("core:home")


class FeedbackListView(views.ListView):
    template_name = "core/feedback_list.html"
    model = core_models.FeedbackModel
    form_class = FeedbackForm
    success_url = reverse_lazy("core:home")


class FeedbackDeleteView(views.ListView):
    template_name = "core/feedback_delete.html"
    model = core_models.FeedbackModel
    form_class = FeedbackForm
    success_url = reverse_lazy("core:home")


class FeedbackDetailView(views.ListView):
    template_name = "core/feedback_detail.html"
    model = core_models.FeedbackModel
    form_class = FeedbackForm
    success_url = reverse_lazy("core:home")


class FeedbackUpdateView(views.ListView):
    template_name = "core/feedback_update.html"
    model = core_models.FeedbackModel
    form_class = FeedbackForm
    success_url = reverse_lazy("core:home")


# ================================= FEEDBACK END ================================= #


# ================================= PRODUCT START ================================= #

# Product list
class ProductListView(views.ListView):
    template_name = "core/product_list.html"
    model = core_models.ProductModel
    context_object_name = "products"


# Product create
class ProductCreateView(views.CreateView):
    template_name = "core/product_create.html"
    model = core_models.ProductModel
    form_class = ProductForm
    success_url = reverse_lazy("core:product_list")


# Product detail
class ProductDetailView(views.DetailView):
    template_name = "core/product_detail.html"
    model = core_models.ProductModel
    context_object_name = "product"


# Product update
class ProductUpdateView(views.UpdateView):
    template_name = "core/product_update.html"
    model = core_models.ProductModel
    form_class = ProductForm
    success_url = reverse_lazy("core:product_list")


# Product delete
class ProductDeleteView(views.DeleteView):
    template_name = "core/product_delete.html"
    model = core_models.ProductModel
    success_url = reverse_lazy("core:product_list")


# ================================= PRODUCT END ================================= #


# ================================= CATEGORY START ================================= #


class ProductByCategoryView(views.ListView):
    template_name = "core/product_list.html"
    model = core_models.ProductModel
    context_object_name = "products"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        pk = self.kwargs.get("pk", None)
        qs = qs.filter(category__id=pk)
        return qs


class CategoryListView(views.ListView):
    template_name = "core/category/category_list.html"
    model = core_models.CategoryModel
    context_object_name = "categories"


# =================================CATEGORY END================================= #

# cart


class AddToCartView(views.View):
    def get(self, request, pk):
        # try:
        user = request.user
        product = core_models.ProductModel.objects.get(id=pk)
        cart, cart_created = core_models.CartModel.objects.get_or_create(
            user=user, checked_out=False
        )
        cart_item, cart_item_created = core_models.CartItemModel.objects.get_or_create(
            cart=cart, product=product
        )
        if not cart_item_created:
            cart_item.quantity += 1

        cart_item.save()
        messages.success(request, "Product added successfully!")
        # except Exception as e:
        #     print(e)
        #     messages.error(request, f"Product couldn't add! ERROR:-{e}")
        url = request.META.get("HTTP_REFERER")
        return redirect(url)


# cart
class CartView(views.TemplateView):
    template_name = "core/checkout/cart.html"


# cartremove
class CartDeleteView(views.DeleteView):
    template_name = "core/checkout/cart_delete.html"
    model = core_models.CartModel


# delivery
class DeliveryView(views.TemplateView):
    model = user_models.AddressModel
    template_name = "core/delivery/delivery_address.html"
    context_object_name = "addresss"


# shipment
class ShipmentView(views.TemplateView):
    template_name = "core/delivery/shipment_details.html"


# order summary


class OrdersummaryView(views.TemplateView):
    template_name = "core/delivery/order_summary.html"


# order placed
class OrderplacedView(views.TemplateView):
    template_name = "core/orderplaced/ordr_placed.html"


# checkout
class CheckoutView(views.TemplateView):
    template_name = "core/checkout/checkout.html"


class CancelorderView(views.TemplateView):
    template_name = "core/checkout/cancelorder.html"


class CanceltemplateView(views.TemplateView):
    template_name = "core/checkout/canceltemplate.html"


# payment
class PaymentView(views.TemplateView):
    template_name = "core/payment/payment.html"


# payment success
class PaymentsuccessView(views.TemplateView):
    template_name = "core/payment/paysuccess.html"


# add more  details
class AdddetailView(views.TemplateView):
    template_name = "core/user/add_details.html"


# add new address
class AddnewaddressView(views.TemplateView):
    template_name = "user/addnew_address.html"
