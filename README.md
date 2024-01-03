Django xhtml2pdf Project to read static files and custom fonts 

I downloaded this code from Dennis Ivy Github (his YouTube: https://www.youtube.com/@DennisIvy).
The base of the code was made by him (templates, URLs, settings).
I added two functions: link_callback and render_pdf_download.
They were created to read static files and custom fonts for the xhtml2pdf library. 
The xhtml2pdf supports only these CSS properties: https://xhtml2pdf.readthedocs.io/en/latest/reference.html. 
So, read this documentation before using it. Have fun!


python -m venv venv


pip install django==4.2.8


pip install xhtml2pdf


python manage.py runserver



checkout settings for static
