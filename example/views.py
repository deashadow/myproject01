from django.shortcuts import render
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
