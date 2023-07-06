import os
import hashlib

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import default_storage
from PIL import Image


@csrf_exempt
def resize_picture(request):
    file = request.FILES.get('file')
    width = int(request.POST.get('width'))
    height = int(request.POST.get('height', 0))

    filename = file.name
    md5_hash = hashlib.md5(filename.encode()).hexdigest()
    extension = os.path.splitext(filename)[1]
    image = Image.open(file)
    if height == 0:
        ratio = width / image.width
        height = int(image.height * ratio)
    modified_filename = f'{md5_hash}_{width}x{height}{extension}'

    modified_filepath = os.path.join(settings.MEDIA_ROOT, modified_filename)

    if not default_storage.exists(modified_filepath):
        image = image.resize((width, height))
        image.save(modified_filepath)

    return JsonResponse({'url': modified_filepath})
