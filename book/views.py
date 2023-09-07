from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import BookForm
from django.core.mail import EmailMessage
# Create your views here.
def book(request):
    bookform=BookForm()
    if request.method == "POST":
        bookform=BookForm(data=request.POST)
        if bookform.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')
            emailBook=EmailMessage(
                "Fiane: Nuevo mensaje de contacto",
                "De {} <{}>\n\nMensaje:\n\n{}".format(name,email,message),
                "najieb-armijos@hotmail.com",
                ["correo-prueba@inbox.mailtrap.io"],
                reply_to=[email]
            )
            try:
                 emailBook.send()
                 return redirect(reverse('book')+"?ok")
            except:
                 return redirect(reverse('book')+"?fail")
            
    return render(request, "book/book.html", {'bookForm':bookform})

