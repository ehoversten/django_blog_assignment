from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
    # return render(request, 'index.html')

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    print("Number is: " + number)
    response = "placeholder to display blog " + str(number)
    return HttpResponse(response)

def edit(request, number):
    print("Editing Blog number " + number)
    response = "placeholder to edit blog " + str(number)
    return HttpResponse(response)

def destroy(request, number):
    print("Deleting Blog entry: " + number)
    return redirect('/')
