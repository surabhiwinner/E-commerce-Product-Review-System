from . import models        

from   django import forms



class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = models.ProductReview
        fields = ['product', 'review_text', 'rating']
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
        }

    def clean_review_text(self):
        review_text = self.cleaned_data.get('review_text')
        
