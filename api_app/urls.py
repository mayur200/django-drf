from django.urls import path
from .views import CartItemViews, HelloView

urlpatterns = [
    path('cart-items/', CartItemViews.as_view()),
    path('cart-items/<int:id>', CartItemViews.as_view()),
    path('hello/', HelloView.as_view(), name='hello'),
]