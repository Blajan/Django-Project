from django.shortcuts import render, redirect, get_object_or_404
from .models import product_sneakers, product_t_shirt, product_hat, product_pant, product_football_sneakers
from django.contrib.auth import login, authenticate
from .forms import (register_user_form, update_user_form, change_password_form,
                    add_sneakers_form, add_t_shirts_form, add_hats_form, add_pants_form, add_football_sneakers_form)
from django.views import generic
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
import os
from django.core.paginator import Paginator


def home(request):
    return render(request, 'appProject/home.html')

def about_me(request):
    return render(request, 'appProject/about_me.html')

# Products
def products_sneakers(request):
    if request.method == 'POST':
        found = request.POST['found']
        filtered_products = product_sneakers.objects.filter(product_name__contains = found)
        grouped = Paginator(filtered_products, 12)
        pagina_num = request.GET.get('page', 1)
        products = grouped.page(pagina_num)
        pages = 'a' * products.paginator.num_pages
        return render(request, 'appProject/sneakers.html', {"found":found, 'products':products, 'pages':pages})
    else:
        all_products = product_sneakers.objects.all()
        grouped = Paginator(all_products, 12)
        pagina_num = request.GET.get('page', 1)
        products = grouped.page(pagina_num)
        pages = 'a' * products.paginator.num_pages
        return render(request, 'appProject/sneakers.html', {'products': products, 'pages':pages})

def products_t_shirts(request):
    if request.method == 'POST':
        found = request.POST['found']
        filtered_products = product_t_shirt.objects.filter(product_name__contains = found)
        grouped = Paginator(filtered_products, 12)
        pagina_num = request.GET.get('page', 1)
        products = grouped.page(pagina_num)
        pages = 'a' * products.paginator.num_pages
        return render(request, 'appProject/t-shirts.html', {"found":found, 'products':products, 'pages':pages})
    else:
        all_products = product_t_shirt.objects.all()
        grouped = Paginator(all_products, 12)
        pagina_num = request.GET.get('page', 1)
        products = grouped.page(pagina_num)
        pages = 'a' * products.paginator.num_pages
        return render(request, 'appProject/t-shirts.html', {"products": products, 'pages':pages})

def products_hats(request):
    if request.method == 'POST':
        found = request.POST['found']
        filtered_products = product_hat.objects.filter(product_name__contains = found)
        grouped = Paginator(filtered_products, 12)
        pagina_num = request.GET.get('page', 1)
        products = grouped.page(pagina_num)
        pages = 'a' * products.paginator.num_pages
        return render(request, 'appProject/hats.html', {"found":found, 'products':products, 'pages':pages})
    else:
        all_products = product_hat.objects.all()
        grouped = Paginator(all_products, 12)
        pagina_num = request.GET.get('page', 1)
        products = grouped.page(pagina_num)
        pages = 'a' * products.paginator.num_pages
        return render(request, 'appProject/hats.html', {"products": products, 'pages':pages})

def products_pants(request):
    if request.method == 'POST':
        found = request.POST['found']
        filtered_products = product_pant.objects.filter(product_name__contains = found)
        grouped = Paginator(filtered_products, 12)
        pagina_num = request.GET.get('page', 1)
        products = grouped.page(pagina_num)
        pages = 'a' * products.paginator.num_pages
        return render(request, 'appProject/pants.html', {"found":found, 'products':products, 'pages':pages})
    else:
        all_products = product_pant.objects.all()
        grouped = Paginator(all_products, 12)
        pagina_num = request.GET.get('page', 1)
        products = grouped.page(pagina_num)
        pages = 'a' * products.paginator.num_pages
        return render(request, 'appProject/pants.html', {"products": products, 'pages':pages})

def products_football_sneakers(request):
    if request.method == 'POST':
        found = request.POST['found']
        filtered_products = product_football_sneakers.objects.filter(product_name__contains = found)
        grouped = Paginator(filtered_products, 12)
        pagina_num = request.GET.get('page', 1)
        products = grouped.page(pagina_num)
        pages = 'a' * products.paginator.num_pages
        return render(request, 'appProject/football_sneakers.html', {"found":found, 'products':products, 'pages':pages})
    else:
        all_products = product_football_sneakers.objects.all()
        grouped = Paginator(all_products, 12)
        pagina_num = request.GET.get('page', 1)
        products = grouped.page(pagina_num)
        pages = 'a' * products.paginator.num_pages
        return render(request, 'appProject/football_sneakers.html', {"products": products, 'pages':pages})

# Login user
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('You have entered a wrong password or username!'))
            return redirect('login')
    else:
        return render(request, 'appProject/login.html')

# Register user
class register_user(generic.CreateView):
    form_class = register_user_form
    template_name = 'appProject/register.html'
    success_url = reverse_lazy('login')

# Update user
def update_user(request):
    submitted = False
    if request.method == 'POST':
        form = update_user_form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/update_user?submitted=True')
    else:
        form = update_user_form(instance=request.user)
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'appProject/update.html', {'form':form, 'submitted':submitted})


# Change password
class change_password(SuccessMessageMixin ,PasswordChangeView):
    form_class = change_password_form
    template_name = 'appProject/change_password.html'
    success_url = reverse_lazy('change_password')
    success_message = 'You have successfully changed your password'


# Add product
class add_sneakers(CreateView):
    form_class = add_sneakers_form
    template_name = 'appProject/add_sneakers.html'
    success_url = reverse_lazy('products_sneakers')


class add_t_shirts(CreateView):
    form_class = add_t_shirts_form
    template_name = 'appProject/add_t-shirts.html'
    success_url = reverse_lazy('products_t-shirts')

class add_hats(CreateView):
    form_class = add_hats_form
    template_name = 'appProject/add_hats.html'
    success_url = reverse_lazy('products_hats')

class add_pants(CreateView):
    form_class = add_pants_form
    template_name = 'appProject/add_pants.html'
    success_url = reverse_lazy('products_pants')

class add_football_sneakers(CreateView):
    form_class = add_football_sneakers_form
    template_name = 'appProject/add_football_sneakers.html'
    success_url = reverse_lazy('products_football_sneakers')

# Delete
def delete_sneakers(request, id):
    object_deleted = product_sneakers.objects.get(pk=id)
    object_deleted.delete()
    return redirect('products_sneakers')

def delete_t_shirts(request, id):
    object_deleted = product_t_shirt.objects.get(pk=id)
    object_deleted.delete()
    return redirect('products_t-shirts')

def delete_hats(request, id):
    object_deleted = product_hat.objects.get(pk=id)
    object_deleted.delete()
    return redirect('products_hats')

def delete_pants(request, id):
    object_deleted = product_pant.objects.get(pk=id)
    object_deleted.delete()
    return redirect('products_pants')

def delete_football_sneakers(request, id):
    object_deleted = product_football_sneakers.objects.get(pk=id)
    object_deleted.delete()
    return redirect('products_football_sneakers')

# Detail
class detail_sneakers(DetailView):
    model = product_sneakers
    template_name = 'appProject/detail_sneakers.html'
    context_object_name = 'detail'

    def get_context_data(self, *args, **kwargs):
        context = super(detail_sneakers, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(product_sneakers, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class detail_t_shirts(DetailView):
    model = product_t_shirt
    template_name = 'appProject/detail_t-shirts.html'
    context_object_name = 'detail'

    def get_context_data(self, *args, **kwargs):
        context = super(detail_t_shirts, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(product_t_shirt, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class detail_hats(DetailView):
    model = product_hat
    template_name = 'appProject/detail_hats.html'
    context_object_name = 'detail'

    def get_context_data(self, *args, **kwargs):
        context = super(detail_hats, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(product_hat, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class detail_pants(DetailView):
    model = product_pant
    template_name = 'appProject/detail_pants.html'
    context_object_name = 'detail'

    def get_context_data(self, *args, **kwargs):
        context = super(detail_pants, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(product_pant, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class detail_football_sneakers(DetailView):
    model = product_football_sneakers
    template_name = 'appProject/detail_football_sneakers.html'
    context_object_name = 'detail'

    def get_context_data(self, *args, **kwargs):
        context = super(detail_football_sneakers, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(product_football_sneakers, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

# Update
def update_sneakers(request, pk):
    post = product_sneakers.objects.get(id=pk)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(post.product_image) > 0:
                os.remove(post.product_image.path)
            post.product_image = request.FILES['image']
        post.product_name = request.POST.get('name')
        post.product_description = request.POST.get('description')
        post.product_price = request.POST.get('price')
        post.save()
        return HttpResponseRedirect(reverse('detail_sneakers', args=[str(pk)]))
    return render(request, 'appProject/update_sneakers.html', {'post': post})


def update_t_shirts(request, pk):
    post = product_t_shirt.objects.get(id=pk)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(post.product_image) > 0:
                os.remove(post.product_image.path)
            post.product_image = request.FILES['image']
        post.product_name = request.POST.get('name')
        post.product_description = request.POST.get('description')
        post.product_price = request.POST.get('price')
        post.save()
        return HttpResponseRedirect(reverse('detail_t-shirts', args=[str(pk)]))
    return render(request, 'appProject/update_t-shirts.html', {'post': post})

def update_hats(request, pk):
    post = product_hat.objects.get(id=pk)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(post.product_image) > 0:
                os.remove(post.product_image.path)
            post.product_image = request.FILES['image']
        post.product_name = request.POST.get('name')
        post.product_description = request.POST.get('description')
        post.product_price = request.POST.get('price')
        post.save()
        return HttpResponseRedirect(reverse('detail_hats', args=[str(pk)]))
    return render(request, 'appProject/update_hats.html', {'post': post})

def update_pants(request, pk):
    post = product_pant.objects.get(id=pk)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(post.product_image) > 0:
                os.remove(post.product_image.path)
            post.product_image = request.FILES['image']
        post.product_name = request.POST.get('name')
        post.product_description = request.POST.get('description')
        post.product_price = request.POST.get('price')
        post.save()
        return HttpResponseRedirect(reverse('detail_pants', args=[str(pk)]))
    return render(request, 'appProject/update_pants.html', {'post': post})

def update_football_sneakers(request, pk):
    post = product_football_sneakers.objects.get(id=pk)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(post.product_image) > 0:
                os.remove(post.product_image.path)
            post.product_image = request.FILES['image']
        post.product_name = request.POST.get('name')
        post.product_description = request.POST.get('description')
        post.product_price = request.POST.get('price')
        post.save()
        return HttpResponseRedirect(reverse('detail_football_sneakers', args=[str(pk)]))
    return render(request, 'appProject/update_football_sneakers.html', {'post': post})



# Like button
def like_view_sneakers(request, pk):
    post = get_object_or_404(product_sneakers, id=request.POST.get('post_id_sneakers'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail_sneakers', args=[str(pk)]))

def like_view_t_shirt(request, pk):
    post = get_object_or_404(product_t_shirt, id=request.POST.get('post_id_t-shirt'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail_t-shirts', args=[str(pk)]))

def like_view_hat(request, pk):
    post = get_object_or_404(product_hat, id=request.POST.get('post_id_hat'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail_hats', args=[str(pk)]))

def like_view_pant(request, pk):
    post = get_object_or_404(product_pant, id=request.POST.get('post_id_pant'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail_pants', args=[str(pk)]))

def like_view_football_sneakers(request, pk):
    post = get_object_or_404(product_football_sneakers, id=request.POST.get('post_id_football_sneakers'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail_football_sneakers', args=[str(pk)]))