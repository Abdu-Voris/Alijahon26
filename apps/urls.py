from django.urls import path, include
from . import views
from .views import HomeListView

urlpatterns = [
    path('', HomeListView.as_view(),name='home'),

]