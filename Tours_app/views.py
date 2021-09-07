from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from Tours_app.forms import LoginForm, SignUpForm, ReviewForm
from Tours_app.models import Tour, Country, Review


class HomePageView(View):
    def get(self, request):
        return render(request, 'base.html')


class GruzjaView(View):
    def get(self, request):
        return render(request, 'gruzja.html')


class KirgistanView(View):
    def get(self, request):
        return render(request, 'kirgistan.html')


class WietnamView(View):
    def get(self, request):
        return render(request, 'wietnam.html')


class AboutPageView(View):
    def get(self, request):
        return render(request, 'about.html')


class TourListView(ListView):
    def get(self, request):
        tours = Tour.objects.all()
        countries = Country.objects.all()
        return render(request, 'tourlist.html', {'objects': tours, 'countries': countries})


class TourDetailsView(DetailView):
    model = Tour
    template_name = 'tourdetails.html'


class AddTourView(CreateView):
    model = Tour
    fields = '__all__'
    template_name = 'touraddform.html'

    def get_success_url(self):
        tour = self.object
        url = reverse('tourlist')
        return url


class UpdateTourView(UpdateView):
    model = Tour
    fields = '__all__'
    template_name = 'tourupdate.html'

    def get_success_url(self):
        tour = self.object
        url = reverse('tourdetails', args=(tour.id,))
        return url


class DeleteTourView(DeleteView):
    model = Tour
    template_name = 'tourdelete.html'
    success_url = reverse_lazy('tourlist')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            login(request, loginForm.user)
            return redirect("/")
        return render(request, 'form.html', {'form': loginForm})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['re-password']
            User.objects.create_user(**form.cleaned_data)
            return redirect('/')
        return render(request, 'form.html', {'form': form})


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'review.html', {'form': form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(**form.cleaned_data)
            return redirect('/')
        return render(request, 'review.html', {'form': form})