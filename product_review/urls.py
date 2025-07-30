from . import views

from django.urls import path


urlpatterns = [
    path('reviews/', views.ProductReviewView.as_view(), name='product_review_list'),
    path('home/',views.HomeView.as_view(), name='home'),

    path('write/', views.WriteReviewView.as_view(), name='write_review'),
]