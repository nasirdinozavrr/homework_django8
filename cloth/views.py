from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms

class ClothListView(ListView):
    queryset = models.ProductCL.objects.all()
    template_name = "clothes_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.all()

class GucciListView(ListView):
    queryset = models.ProductCL.objects.filter(
        tags__name="Gucci").order_by("-id")
    template_name = "gucci_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(
            tags__name="Gucci").order_by("-id")


class SupremeListView(ListView):
    queryset = models.ProductCL.objects.filter(
        tags__name="Supreme").order_by("-id")
    template_name = "supreme_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(
            tags__name="Supreme").order_by("-id")

class NikeListView(ListView):
    queryset = models.ProductCL.objects.filter(
        tags__name="Nike").order_by("-id")
    template_name = "nike_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(
            tags__name="Nike").order_by("-id")


class AdidasListView(ListView):
    queryset = models.ProductCL.objects.filter(
        tags__name="Adidas").order_by("-id")
    template_name = "adidas_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(
            tags__name="Adidas").order_by("-id")


class ClothDetailView(DetailView):
    template_name = "clothes_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.ProductCL, id=product_id)


class OrderCreateView(CreateView):
    template_name = "add_order.html"
    form_class = forms.OrderForm
    success_url = "/clothes/"
    queryset = models.OrderCL.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)

