from core import models as core_models


def common_data(request):
    user = request.user
    cart=None
    if user.is_authenticated:
        cart = core_models.CartModel.objects.filter(user=user, checked_out=False).last()
    context = {
        "cart": cart,
    }
    return context