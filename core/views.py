from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")
def about(request):
    return render(request, "core/about.html")
def book(request):
    return render(request, "core/book.html")
def menu(request):
    return render(request, "core/menu.html")