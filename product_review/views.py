from django.shortcuts import render
from .models import ProductReview, Product, Profile

from .forms import ProductReviewForm
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
        form = ProductReviewForm()
        products = Product.objects.all()  # Fetch products for dropdown

        data = {
            'form': form,
            'products': products,
            'page': 'write_review_page',
        }

        return render(request, 'product_review/review_form.html', context=data)
    
    def post(self, request, *args, **kwargs):
        form = ProductReviewForm(request.POST, request.FILES)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Make sure the user is logged in
            review.save()
            return render(request, 'product_review/review_list.html', {'review': review})
        else:
            return render(request, 'product_review/review_form.html', {'form': form, 'page': 'write_review_page'})