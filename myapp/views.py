from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import UploadImageForm
from django.core.files.storage import default_storage
from PIL import Image
import pytesseract
import os

#def home(request):
#    return HttpResponse("Hello, Django!")

#def home(request):
#    return render(request, 'myapp/index.html')

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


def upload_and_process_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            try:

                tesseract_path = r'Inkwise\myapp\static\Tesseract-OCR\tesseract.exe'
                if os.path.exists(tesseract_path):
                    pytesseract.pytesseract.tesseract_cmd = tesseract_path
                else:
                    print(f"Warning: Tesseract not found at {tesseract_path}. Ensure it's in your PATH.")
                # --- End of Path Configuration ---

                # Save the uploaded image temporarily
                temp_image_path = default_storage.save('temp_image.jpg', image)  # Or .png, etc.
                img = Image.open(default_storage.path(temp_image_path))
                extracted_text = pytesseract.image_to_string(img)

                # Optionally, delete the temporary file (or keep it if needed)
                default_storage.delete(temp_image_path)

                context = {'text': extracted_text}
                return render(request, 'result.html', context)

            except Exception as e:
                # Log the error for debugging (very important in production)
                print(f"Error processing image: {e}")
                return HttpResponse(f"Error processing image: {e}")
        else:
            # Form is invalid
            return render(request, 'pricing.html', {'form': form, 'error': 'Invalid form. Please upload a valid image.'})
    else:
        # GET request
        form = UploadImageForm()
        return render(request, 'pricing.html', {'form': form})