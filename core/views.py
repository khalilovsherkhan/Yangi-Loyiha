from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home (request):
    data = Post.objects.all()
    context = {
        'data':data}
    return render(request, 'index.html', context)
def formpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model_ro'yxati')
 else:
        forma= MeningModelFormasi()
    return render(request, 'form.html',{'forma': forma})
        

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
def blog_category_05(request):
    return render(request, 'blog_category_05.html')
def blog_category_06(request):
    return render(request, 'blog_category_06.html')
