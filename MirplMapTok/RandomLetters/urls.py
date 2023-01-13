from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('print-random-leters/', views.random_index, name='random_index'),

    # print-random-leters/?size_from=50&size_to=70
]