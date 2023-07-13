# qrcodeapp/views.py

from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
from.forms import ContactForm


def generate_qrcode(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = {
                "name": form.data["name"],
                "email": form.data["email"]
            }
            # print(data)
            img = make(data)
            img_name = 'qr' + str(time.time()) + '.png'
            img.save(settings.MEDIA_ROOT + '/' + img_name)
            return render(request, 'index.html', {'img_name': img_name, "data": data})
    return render(request, 'index.html', {"form": form})