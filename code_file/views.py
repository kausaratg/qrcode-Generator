from django.shortcuts import render
import qrcode
from time import time
from django.conf import settings
# Create your views here.

def qrcode_generator(request):
    if request.method == 'POST':
        mylink =request.POST['link']
        qr = qrcode.make(mylink, box_size=7)
        qr_name = f'{str(time())}.png'
        qr.save(settings.MEDIA_ROOT +'/'+ qr_name)
        context = {'qr_name':qr_name}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')