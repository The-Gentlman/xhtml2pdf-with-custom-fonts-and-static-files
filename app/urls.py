from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('view_html/', views.viewhtml, name="view_html"),
    path('render_pdf_download/', views.render_pdf_download,
         name='render_pdf_download'),

]
