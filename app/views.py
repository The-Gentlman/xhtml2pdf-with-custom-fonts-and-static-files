from django.contrib.staticfiles import finders
from django.conf import settings
import os
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from xhtml2pdf.files import pisaFileObject
from django.core.handlers.wsgi import WSGIRequest

"""
I downloaded this code from Dennis Ivy Github (his YouTube: https://www.youtube.com/@DennisIvy).
The base of the code was made by him (templates, URLs, settings).
I added two functions: link_callback and render_pdf_download.
They were created to read static files and custom fonts for the xhtml2pdf library.
The xhtml2pdf supports only these CSS properties:
https://xhtml2pdf.readthedocs.io/en/latest/reference.html.
So, read this documentation before using it. 
Have fun!
"""


def index(request):
    context = {}
    return render(request, 'app/index.html', context)


def viewhtml(request):
    context = {}
    return render(request, 'app/template.html', context)


data = {
    "company": "Dennnis Ivanov Company",
    "address": "123 Street name",
    "city": "Vancouver",
    "state": "WA",
    "zipcode": "98663",


    "phone": "555-555-2345",
    "email": "youremail@dennisivy.com",
    "website": "dennisivy.com",
}


def link_callback(uri, rel=None):
    if isinstance(uri, WSGIRequest):
        path = uri.get_full_path()
    if uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT,
                            uri.replace(settings.STATIC_URL, ""))
    else:
        path = uri
    if not os.path.isfile(path):
        raise Exception(f"Path does not exist: {path}")
    pisaFileObject.getNamedFile = lambda self: path
    print(path)
    return path


def render_pdf_download(request):
    template_path = 'app/template.html'
    context = data
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html,
        dest=response,
        link_callback=link_callback
    )
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
