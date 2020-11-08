""" class Book( models.Model):
    title = models.CharField( max_length=40);
    description = models.CharField( max_length=100); 
    price = models.DecimalField( max_digits=6, decimal_places=2); """



from django import forms
from .models import Book 
from .models import Account
from .models import Person

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'price']

class AccountForm ( forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username','password','displayname']
        widgets = {
            'username': forms.TextInput( 
                attrs= {
                    'placeholder': 'enter a username'
                }
            ),
            'password': forms.PasswordInput()
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields = ['fname', 'lname', 'age']  
        labels = {'fname': 'First Name','lname': 'Last Name' }


