
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import UploadImageForm
from django.core.files.storage import default_storage
from PIL import Image
import pytesseract

#def home(request):
 #   return HttpResponse("Hello, Django!")

#def home(request):
   # return render(request, 'myapp/index.html')

def index(request):
    return render(request, 'index.html')

def pricing(request):
    return render(request, 'pricing.html')

def team(request):
    return render(request, 'team.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            # Save the image
            image_name = default_storage.save('uploaded_images/' + image.name, image)
            image_path = default_storage.path(image_name)

            # Process the image
            try:
                pil_image = Image.open(image_path)
                text = pytesseract.image_to_string(pil_image)
            except Exception as e:
                return HttpResponse(f"Error processing image: {e}")

            return HttpResponse(f"Image uploaded and processed. Recognized text: {text}")
    else:
        form = UploadImageForm()
    return render(request, 'upload.html', {'form': form})