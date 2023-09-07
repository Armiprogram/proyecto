from django.shortcuts import render, get_object_or_404
from .models import About, Category
# Create your views here.
def about(request):
    abouts= About.objects.all()
    return render(request, "about/about.html", {'listAbout':abouts})

def category(request, categoryId): 
   # category=Category.objects.get(id=categoryId)
    category=get_object_or_404(Category, id=categoryId)
    abouts=About.objects.filter(categories=category)
    return render(request, "about/category.html", {'listAbout':abouts })