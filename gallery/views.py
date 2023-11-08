from django.shortcuts import render, redirect
from .forms import GalleryForm
from .models import Gallery


def homepage(request):
    form = GalleryForm()
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("/")
    galleries = Gallery.objects.all()
    return render(request, 'homepage.html', {'form': form, 'galleries': galleries})
