from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .forms import BookForm
from .models import Book
from .models import Account
from .forms import AccountForm, PersonForm
from .models import Person

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

def listUsers( request):
    users = Account.objects.all();
    context = {'users': users};
    return render( request, 'example/users.html', context)
    
def addUser( request):
    if request.method == "GET":
        accountForm = AccountForm();
    elif request.method == "POST":
        accountForm = AccountForm(request.POST)
        if accountForm.is_valid() == False:
            return HttpResponse(accountForm.errors)
        username = accountForm.cleaned_data['username']
        password = accountForm.cleaned_data['password']
        displayname = accountForm.cleaned_data['displayname']
        print( '{}, {}, {}'.format( username, password, displayname))
        accountForm.save();
        return redirect( '/users')

    context = { 'accountForm': accountForm}
    return render( request, 'example/user.html', context)
 

def about( request):
    return render( request, 'example/about.html')

def contact( request):
    return render( request, 'example/contact.html')

def person( request):
    if request.method=="GET":
        personForm = PersonForm()
        context = {'personForm': personForm}
    #print("id="+str(id))
    #person = Person.objects.get(id=id)
        context = {  'personForm': personForm}
        return render( request, 'example/person.html', context) 
    elif request.method=="POST":
        personForm=PersonForm(request.POST)
        if personForm.is_valid()==False:
            return HttpResponse(personForm.errors)
        personForm.save()
        return redirect('http://localhost:8000/persons')


def updateperson( request, id=None):
    if request.method=="GET":
        person = get_object_or_404(Person, id=id)
        personForm = PersonForm(instance=person)
        context = {'personForm': personForm}
    #print("id="+str(id))
    #person = Person.objects.get(id=id)
        context = {  'personForm': personForm}
        return render( request, 'example/updateperson.html', context) 
    elif request.method=="POST":
        personForm=PersonForm(request.POST)
        if personForm.is_valid()==False:
            return HttpResponse(personForm.errors)
        personForm.save()
        return redirect('http://localhost:8000/persons')

def deleteperson( request, id):
    if request.method=="GET":
        person = get_object_or_404(Person, id=id)
        person.delete()
        return redirect('http://localhost:8000/persons')



def persons( request):
        persons = Person.objects.all()
        context = {'persons': persons}
    #print("id="+str(id))
    #person = Person.objects.get(id=id)
        return render( request, 'example/persons.html', context) 
        



def editUser(request, id):
    print('editUser: id='+ str(id))
    if request.method == "GET":
        account = get_object_or_404( Account, id=id)
        print('account=' +str(account))
        accountForm = AccountForm( initial={'username': account.username,
          'password': account.password, 'displayname': account.displayname});
    elif request.method == "POST":
        accountForm = AccountForm(request.POST)
        if accountForm.is_valid() == False:
            return HttpResponse(accountForm.errors)
        username = accountForm.cleaned_data['username']
        password = accountForm.cleaned_data['password']
        displayname = accountForm.cleaned_data['displayname']
        print( '{}, {}, {}'.format( username, password, displayname))
        accountForm.save();
        return redirect( '/users')


    context = { 'accountForm': AccountForm}
    return render ( request, 'example/editUser.html', context)


def getTotal(request):
    print('inside getTotal')
    persons = Person.objects.all()
    total = 0
    for person in persons: 
        total = total+int(person.age)
    print('total='+str(total))
    return JsonResponse({'total': total})

       
    