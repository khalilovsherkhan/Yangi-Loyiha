from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'index.html')

def blog_author(request):
    return render(request,'blog-autor.html')
def page(request):
    return render(request, 'page.html')
def blog_category_02(request):
    return render(request, 'blog_category_02.html')
def blog_category_03(request):
    return render(request, 'blog_category_03.html')
def blog_category_04(request):
    return render(request, 'blog_category_04.html')
def blog_category_04(request):
    return render(request, blog_category_04(2).html)
def blog_category_05(request):
    return render(request, 'blog_category_05.html')
def blog_category_06(request):
    return render(request, 'blog_category_06.html')
