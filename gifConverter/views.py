from django.http import HttpResponse
from django.shortcuts import render

from PIL import Image, ImageSequence
import io
import base64


# Create your views here.
def index(request):
    if request.method == 'POST' and request.FILES.get('gif'):
        gif_file = request.FILES['gif']
        try:
            im = Image.open(gif_file)
        except Exception:
            return render(request, 'gifConverter/index.html', {'error': 'Invalid image file'})

        frames = []
        durations = []
        for frame in ImageSequence.Iterator(im):
            frames.append(frame.convert('RGBA').copy())
            durations.append(frame.info.get('duration', im.info.get('duration', 100)))

        if not frames:
            return render(request, 'gifConverter/index.html', {'error': 'No frames found in GIF'})

        out = io.BytesIO()
        first_frame, other_frames = frames[0], frames[1:]

        save_kwargs = {
            'format': 'WEBP',
            'save_all': True,
            'append_images': other_frames,
            'duration': durations,
            'loop': 0,
        }

        try:
            first_frame.save(out, **save_kwargs)
        except Exception:
            return render(request, 'gifConverter/index.html', {'error': 'Conversion failed. Ensure Pillow is built with WebP support.'})

        out.seek(0)
        webp_bytes = out.getvalue()
        webp_b64 = base64.b64encode(webp_bytes).decode('ascii')

        return render(request, 'gifConverter/index.html', {'webp_b64': webp_b64})

    return render(request, 'gifConverter/index.html')