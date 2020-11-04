from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import BookForm
from .models import Book

def book( request):
    if request.method == "POST":
        form = BookForm( request.POST)
        if form.is_valid() == False:
            print(form.errors);
            return HttpResponse(form.errors)
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        price = float(form.cleaned_data['price'])
        print( "title="+title+",description="+description+",price="+str(price))
        form.save();
    else:   #request . method == "GET"
        form = BookForm();
    context = { 'form': form};
    return render( request, 'example/book.html', context)



# Createfrom django.shortcuts import render
from example.models import Person

# Create your views here.
def home( request):
    return render( request, 'example/home.html')

def about( request):
    return render( request, 'example/about.html')

def person( request, id):
    print("id="+str(id))
    person = Person.objects.get(id=id)
    context = { 'id' : id, 'person': person}
    return render( request, 'example/person.html', context) 
