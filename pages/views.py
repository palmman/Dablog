from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, AddBlogForm
from .models import Blog, Account
from django.contrib import messages, auth

# Create your views here.

def home(request):
    current_user = request.user
    blogs = Blog.objects.all().order_by('-date_created')
    if request.method == 'POST':
            form = AddBlogForm(request.POST)
            if form.is_valid():
                title = request.POST['title']
                content = request.POST['content']   
                image = request.FILES.get('image', None)   
                blog = Blog.objects.create(user=current_user, title=title, content=content, image=image)
                blog.save()
                messages.success(request, 'Blog Added.')
                return redirect('home')
    else:
        form = AddBlogForm()

    context = {
        'blogs' : blogs,
        'form' : form,
    }
    return render(request, 'home.html', context)

def blog_detail(request, slug):

    blog = get_object_or_404(Blog, slug = slug)
    # blog = Blog.objects.get(slug = slug)

    context = {
        'blog' : blog,
    }
    return render(request, 'pages/blog_detail.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are Logged in.')
            return redirect('home')
        else:
            print('5555')
            messages.error(request, 'The username or password is incorrect')
            return redirect('login')
        
    return render(request, 'pages/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']       
            user = Account.objects.create_user( username=username, name=name, email=email, password=password)
            user.save()
            auth.login(request, user)
            messages.success(request, 'Thank you for registering with us.')
            return redirect('register')
    else:
        form = RegistrationForm()

    context = {
        'form' : form,
    }
    return render(request, 'pages/register.html', context)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')
    