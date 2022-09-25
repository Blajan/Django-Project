from django.urls import path
from .views import (home, about_me, register_user, change_password,add_sneakers, add_t_shirts, add_hats, add_pants,
                    add_football_sneakers, update_sneakers, detail_football_sneakers, detail_pants, detail_hats,
                    detail_t_shirts, detail_sneakers)
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_me, name='about'),
    path('sneakers/', views.products_sneakers, name='products_sneakers'),
    path('t-shirts/', views.products_t_shirts, name='products_t-shirts'),
    path('hats/', views.products_hats, name='products_hats'),
    path('pants/', views.products_pants, name='products_pants'),
    path('football_sneakers/', views.products_football_sneakers, name='products_football_sneakers'),
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='appProject/logout.html'), name="Logout"),
    path('register_user/', register_user.as_view(), name='register_user'),
    path('update_user/', views.update_user, name='update_user'),
    path('password/', change_password.as_view(), name='change_password'),

    path('add_sneakers/', add_sneakers.as_view(), name='add_sneakers'),
    path('add_t-shirts/', add_t_shirts.as_view(), name='add_t-shirts'),
    path('add_hats/', add_hats.as_view(), name='add_hats'),
    path('add_pants/', add_pants.as_view(), name='add_pants'),
    path('add_football_sneakers/', add_football_sneakers.as_view(), name='add_football_sneakers'),

    path('delete_sneakers/<int:id>/', views.delete_sneakers, name='delete_sneakers'),
    path('delete_t-shirts/<int:id>/', views.delete_t_shirts, name='delete_t-shirts'),
    path('delete_hats/<int:id>/', views.delete_hats, name='delete_hats'),
    path('delete_pants/<int:id>/', views.delete_pants, name='delete_pants'),
    path('delete_football_sneakers/<int:id>/', views.delete_football_sneakers, name='delete_football_sneakers'),

    path('detail_sneakers/<int:pk>/', detail_sneakers.as_view(), name='detail_sneakers'),
    path('detail_t-shirts/<int:pk>/', detail_t_shirts.as_view(), name='detail_t-shirts'),
    path('detail_hats/<int:pk>/', detail_hats.as_view(), name='detail_hats'),
    path('detail_pants/<int:pk>/', detail_pants.as_view(), name='detail_pants'),
    path('detail_football_sneakers/<int:pk>/', detail_football_sneakers.as_view(), name='detail_football_sneakers'),

    path('update_sneakers/<int:pk>/', views.update_sneakers, name='update_sneakers'),
    path('update_t-shirts/<int:pk>/', views.update_t_shirts, name='update_t-shirts'),
    path('update_hats/<int:pk>/', views.update_hats, name='update_hats'),
    path('update_pants/<int:pk>/', views.update_pants, name='update_pants'),
    path('update_football_sneakers/<int:pk>/', views.update_football_sneakers, name='update_football_sneakers'),

    path('like_sneakers/<int:pk>/', views.like_view_sneakers, name='like_post_sneakers'),
    path('like_t-shirt/<int:pk>/', views.like_view_t_shirt, name='like_post_t-shirt'),
    path('like_hat/<int:pk>/', views.like_view_hat, name='like_post_hat'),
    path('like_pant/<int:pk>/', views.like_view_pant, name='like_post_pant'),
    path('like_football_sneakers/<int:pk>/', views.like_view_football_sneakers, name='like_post_football_sneakers'),
]
