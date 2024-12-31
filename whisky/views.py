# whisky/views.py
from django.views.generic import ListView, DetailView, FormView
from .models import Whisky
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.db.models import Q

class WhiskyListView(ListView):
    model = Whisky
    template_name = 'whisky/whisky_list.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Whisky.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)    
            )
        return Whisky.objects.all()
        
class WhiskyDetailView(DetailView):
    model = Whisky
    template_name = 'whisky/whisky_detail.html'
    context_object_name = 'whisky'  # 템플릿에서 사용할 컨텍스트 변수 이름 설정

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('whisky_list')
    else:
        form = SignUpForm()
    return render(request, 'whisky/signup.html', {'form': form})
