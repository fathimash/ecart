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
    path("product_by_category/<int:pk>/list/",views.ProductByCategoryView.as_view(), name="product_by_category",),
   
    # Cart
    path("cart/product/<int:pk>/add/", views.AddToCartView.as_view(), name="add_to_cart"),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("cart_delete/", views.CartView.as_view(), name="cart_delete"),

    # delivery
    path("delivery/", views.DeliveryView.as_view(), name="delivery"),
    # shipment
    path("shipment/", views.ShipmentView.as_view(), name="shipment"),
    # ordersummary
    path("ordersummary/", views.OrdersummaryView.as_view(), name="ordersummary"),
    #orderplaced
     path("ordr_placed/", views.OrderplacedView.as_view(), name="ordr_placed"),
    # checkout
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    # cancelorder
    path("cancelorder/", views.CancelorderView.as_view(), name="cancelorder"),
     # canceltemplate
    path("canceltemplate/", views.CanceltemplateView.as_view(), name="canceltemplate"),
    # payment
    path("payment/", views.PaymentView.as_view(), name="payment"),
    # payment success
    path("paymentsuccess/", views.PaymentsuccessView.as_view(), name="paymentsuccess"),
    path("add_details/", views.AdddetailView.as_view(), name="add_details"),
    path("addnew_address/", views.AddnewaddressView.as_view(), name="addnew_address"),
    #dashboard
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    #search
    path("product/search/",views.ProductSearchView.as_view(),name="product_search"),



]