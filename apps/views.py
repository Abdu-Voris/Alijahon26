from django.conf.global_settings import TEMPLATES
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from apps.models import Product, Category


class HomeListView(ListView):
    queryset = Product.objects.all().order_by('-created_at')
    template_name = 'apps/home.html'
    context_object_name = 'products'



    def get_context_data(self, *, object_list=None, **kwargs):
        data =  super().get_context_data(object_list=object_list, **kwargs)
        data['categories'] = Category.objects.all()
        return data


