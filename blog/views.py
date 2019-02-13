# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.
def home(request):
        blogs = Blog.objects 
        blog_list = Blog.objects.all().reverse() # 블로그 객체 다 가져오기
        paginator = Paginator(blog_list, 6) # 3개씩 잘라내기
        page = request.GET.get('page') # 페이지 번호 알아오기
        if page is None:
                page = 1
        else:
                page = int(page)
        firstPage= (page//10) * 10 +1   # 페이지 시작
        LastPage= firstPage+10           # 페이지 끝
        posts = paginator.get_page(page) # 페이지 번호 인자로 넘겨주기
        count = [1,2,3]
        if LastPage>posts.paginator.num_pages:
                LastPage=posts.paginator.num_pages+1
        pageRange=range(firstPage,LastPage)
        return render(request, 'home.html', {'blogs' :blogs, 'posts': posts, 'pageRange':pageRange, 'count':count})

# 블로그 글 상세읽기
def detail(requset,blog_id):
        blog_detail = get_object_or_404(Blog,pk=blog_id) # 해당 객체 반환
        return render(requset,'detail.html',{'blog':blog_detail})

# 새 블로그 글 만들기
def new(request):
        return render(request, 'new.html')

def create(request):
        blog = Blog()
        blog.title = request.GET['title']
        blog.body = request.GET['body']
        blog.username = request.GET['username']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/' + str(blog.id))