import re

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from django.views.generic import FormView


from .models import Product, BaseRank, DesiredRank
from .forms import RankSelectionForm
from . import serializers


class StoreFormView(FormView):
    template_name = 'store.html'
    form_class = RankSelectionForm

    def get_context_data(self, **kwargs):
        context = super(StoreFormView, self).get_context_data(**kwargs)

        if ('base_rank' in self.request.get_full_path()) and ('desired_rank' in self.request.get_full_path()):
            url = re.findall('[0-9][0-9]|[0-9]|[0-9][0-9]', self.request.get_full_path())
            context['products_list'] = Product.objects.filter(base_rank=url[0]).filter(desired_rank=url[1])

        return context

class ProductsAPIView(ListAPIView):
    serializer_class = serializers.ProductsSerializer

    def get_queryset(self):
        products = Product.objects.all()

        return products

class BaseRanksAPIView(ListAPIView):
    serializer_class = serializers.BaseRanksSerializer

    def get_queryset(self):
        base_ranks = BaseRank.objects.all()

        return base_ranks

class DesiredRanksAPIView(ListAPIView):
    serializer_class = serializers.DesiredRanksSerializer

    def get_queryset(self):
        desired_ranks = DesiredRank.objects.all()

        return desired_ranks

class ProductDetailAPIView(APIView):

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = serializers.ProductDetailSerializer(product)

        return Response(serializer.data)
