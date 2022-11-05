from django.urls import path
from core import views

app_name = "core"
urlpatterns = [
    # Common
    path("", views.HomeView.as_view(), name="home"),
    path("about_us/", views.AboutView.as_view(), name="about_us"),
    # Feedback
    path(
        "feedback/create/", views.FeedbackCreateView.as_view(), name="feedback_create"
    ),
    path("feedback/list/", views.FeedbackListView.as_view(), name="feedback_list"),
    path(
        "feedback/<int:pk>/delete/",
        views.FeedbackDeleteView.as_view(),
        name="feedback_delete",
    ),
    path(
        "feedback/<int:pk>/detail/",
        views.FeedbackDetailView.as_view(),
        name="feedback_detail",
    ),
    path(
        "feedback/<int:pk>/update/",
        views.FeedbackUpdateView.as_view(),
        name="feedback_update",
    ),
    # Product
    path("product/list/", views.ProductListView.as_view(), name="product_list"),
    path("product/create/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/detail/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "product/<int:pk>/update/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "product/<int:pk>/delete/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
    # category
    path("category/list/", views.CategoryListView.as_view(), name="category_list"),
    path(
        "product_by_category/<int:pk>/list/",
        views.ProductByCategoryView.as_view(),
        name="product_by_category",
    ),
    # Cart
    path(
        "cart/product/<int:pk>/add/", views.AddToCartView.as_view(), name="add_to_cart"
    ),
    # delivery
    path("delivery/", views.DeliveryView.as_view(), name="delivery"),
    # shipment
    path("shipment/", views.ShipmentView.as_view(), name="shipment"),
    # ordersummary
    path("ordersummary/", views.OrdersummaryView.as_view(), name="ordersummary"),
    # checkout
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    # payment
    path("payment/", views.PaymentView.as_view(), name="payment"),
    # user
    path("user/", views.UserView.as_view(), name="user"),
    # user
    path("add_details/", views.AdddetailView.as_view(), name="add_details"),
]
