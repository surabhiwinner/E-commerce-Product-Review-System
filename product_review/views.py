from django.shortcuts import render
from .models import ProductReview, Product, Profile
# Create your views here.
from django.views import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'product_review/home.html', {})
    

class ProductReviewView(View):
    def get(self, request, *args, **kwargs):
        # Logic to retrieve product reviews
        
        product = Product.objects.all()
        reviews = ProductReview.objects.all()

        data = {
            'reviews': reviews,
            'products': product,
            'page' : 'product_review_list_page',
        }

        return render(request, 'product_review/review_list.html', context=data)

    def post(self, request, *args, **kwargs):
        # Logic to submit a new product review
        return render(request, 'product_review/review_submit.html', {})
    


class WriteReviewView(View):
    def get(self, request, *args, **kwargs):
        # Logic to display the review form
        return render(request, 'product_review/review_form.html', {})
    
    def post(self, request, *args, **kwargs):
        # Logic to handle the form submission
        return render(request, 'product_review/review_submit.html', {})
    