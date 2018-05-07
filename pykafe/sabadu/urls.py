from django.urls import url
from myapp.views import Index

from . import views

urlpatterns = [
    url(r'', Index.as_view(), name='index'),
]
