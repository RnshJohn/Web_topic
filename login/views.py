from django.shortcuts import render
from .form import *
from .models import userdb
# Create your views here.


def showimage(request):
    name = userdb.objects.last()

    imagefile = name.imagefile

    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'imagefile': imagefile,
               'form': form
               }

    return render(request, 'Blog/images.html', context)
