from django import forms
from core import models


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.FeedbackModel
        # fields = "__all__" #["name", "message", "email", ]
        exclude = ('status', )
 #product

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.ProductModel
        # fields = "__all__" #["name", "message", "email", ]
        exclude = ("status","created_on","updated_on" )

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.ProductModel
        # fields = "__all__" #["name", "message", "email", ]
        exclude = ("status","created_on","updated_on" )

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.CategoryModel
        # fields = "__all__" #["name", "message", "email", ]
        exclude = ("status","created_on","updated_on" )

