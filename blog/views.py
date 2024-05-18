from django.shortcuts import render


def blogs_page(request):
    return render(request, 'blog/blogs-page.html')


def single(request):
    return render(request, 'blog/single-blog.html')

# Create your views here.
