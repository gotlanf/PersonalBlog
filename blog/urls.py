from django.urls import path
from blog.views import *

urlpatterns = [
    path('blog/', blogs_page),
    path('single/', single)
]