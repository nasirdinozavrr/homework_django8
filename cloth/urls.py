from django.urls import path
from . import views

app_name = "name"
urlpatterns = [
    path("clothes/", views.ClothListView.as_view(), name="clothes_list"),
    path("supreme/", views.SupremeListView.as_view(), name="supreme_list"),
    path("nike/", views.NikeListView.as_view(), name="nike_list"),
    path("adidas/", views.AdidasListView.as_view(), name="adidas_list"),
    path("gucci/", views.GucciListView.as_view(), name="gucci_list"),
    path("add-order/", views.OrderCreateView.as_view(), name="order_create"),
    path(
        "name/<int:id>/", views.ClothDetailView.as_view(),
        name="clothes_detail"
    ),
]
