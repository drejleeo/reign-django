from django.urls import include, path
from waves import views

urlpatterns = [
    path('', views.index_view, name='index'),
]
