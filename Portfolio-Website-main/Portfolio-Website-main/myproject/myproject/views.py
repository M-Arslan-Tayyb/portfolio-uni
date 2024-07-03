from django.http import HttpResponse
from django.shortcuts import render
from contact.models import contact
from Introduction.models import intro


def homepage(request):
    personal_data = intro.objects.all()
    data = {
        "personal_data": personal_data
    }
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')  # Storing the data in database
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        en = contact(name=name, email=email, subject=subject, message=message)
        en.save()
    return render(request, "index.html", data)

