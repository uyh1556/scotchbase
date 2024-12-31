from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.WhiskyListView.as_view(), name='whisky_list'),
    path('<int:pk>/', views.WhiskyDetailView.as_view(), name='whisky_detail'),
    path('search/', views.WhiskyListView.as_view(), name='search'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='whisky/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='whisky_list'), name='logout'),
]
