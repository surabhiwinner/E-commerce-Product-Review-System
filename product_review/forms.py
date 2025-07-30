from . import models         
from django import forms

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = models.ProductReview
        fields = ['product', 'comment', 'rating']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
        }

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        # add custom validation logic here, if needed
        return comment
