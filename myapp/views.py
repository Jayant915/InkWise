from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import UploadImageForm
from django.core.files.storage import default_storage
from PIL import Image
import pytesseract
import os
import requests

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
                # Save uploaded image temporarily
                temp_image_path = default_storage.save('temp_uploaded_image.jpg', image)
                image_file_path = default_storage.path(temp_image_path)

                # Prepare the API request
                with open(image_file_path, 'rb') as img_file:
                    response = requests.post(
                        'https://api.ocr.space/parse/image',
                        files={'filename': img_file},
                        data={
                            'apikey': 'K81632843188957',
                            'language': 'eng',
                            'OCREngine': 2
                        }
                    )
                    response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

                # Clean up temp file
                default_storage.delete(temp_image_path)

                # Process response
                result = response.json()
                extracted_text = ""
                if "ParsedResults" in result and isinstance(result["ParsedResults"], list) and len(result["ParsedResults"]) > 0:
                    first_result = result["ParsedResults"][0]
                    if "ParsedText" in first_result:
                        extracted_text = first_result["ParsedText"]
                    else:
                        print("Warning: 'ParsedText' key not found in the first ParsedResult.")
                        extracted_text = "Could not extract text from the image."
                else:
                    print("Warning: 'ParsedResults' not found or is empty in the API response.")
                    extracted_text = "Could not process the image."

                context = {'text': extracted_text}
                return render(request, 'result.html', context)

            except requests.exceptions.RequestException as e:
                print(f"Error during OCR API request: {e}")
                return HttpResponse(f"Error processing image: Could not connect to the OCR service.")
            except Exception as e:
                print(f"Error processing OCR API response: {e}")
                return HttpResponse(f"Error processing image: An unexpected error occurred.")
        else:
            return render(request, 'pricing.html', {'form': form, 'error': 'Invalid form. Please upload a valid image.'})
    else:
        form = UploadImageForm()
        return render(request, 'pricing.html', {'form': form})