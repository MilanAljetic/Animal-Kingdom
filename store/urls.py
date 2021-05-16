from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_animals, name='all_animals'),
    path('item/<slug:slug>/', views.animal_detail, name='animal_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]
