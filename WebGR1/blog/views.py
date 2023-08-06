import sqlite3
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News


def blog_list(request):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM news')
    data = cursor.fetchall()
    # phân trang 
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    conn.close()
    context = {'page_obj': page_obj}
    return render(request, 'blog/blog.html', context)



# from django.shortcuts import render
# from .models import Post
# # Create your views here.
# def list(request):
#     Data = {'Posts':Post.objects.all().order_by("-date") } 
#     return render(request, 'blog/blog.html', Data)

# def post(request, id):
#     post= Post.objects.get(id = id)
#     return render(request, 'blog/post.html', {'post': post})

# from django.shortcuts import render
# from .models import Blog

# def blog_list(request):
#     blogs = Blog.objects.all()
#     context = {'blogs': blogs}
#     return render(request, 'blog/blog.html', context)

