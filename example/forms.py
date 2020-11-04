""" class Book( models.Model):
    title = models.CharField( max_length=40);
    description = models.CharField( max_length=100); 
    price = models.DecimalField( max_digits=6, decimal_places=2); """



from django import forms
from .models import Book 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'price']