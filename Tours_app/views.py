from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.conf import settings

from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from Tours_app.forms import LoginForm, SignUpForm, EmailForm
from Tours_app.models import Tour, Review, Category, UserReservation


class HomePageView(View):
    def get(self, request):
        return render(request, 'base.html')


class AboutPageView(View):
    def get(self, request):
        return render(request, 'about.html')


class TourListView(ListView):
    def get(self, request):
        tours = Tour.objects.filter(id__lte=-1)
        types = Category.objects.all()
        return render(request, 'tourlist.html', {'objects':tours , 'types': types})


class CategoryListView(View):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        return render(request, 'categories.html', {'category': category})


class AddTourView(CreateView):
    model = Tour
    fields = ['tour_name', 'tour_days', 'tour_start', 'tour_end', 'category', 'tour_price']
    template_name = 'touraddform.html'

    def get_success_url(self):
        tour = self.object
        url = reverse('tourlist')
        return url


class UpdateTourView(UpdateView):
    model = Tour
    fields = ['tour_name', 'tour_days', 'tour_start', 'tour_end', 'category', 'tour_price']
    template_name = 'tourupdate.html'

    def get_success_url(self):
        tour = self.object
        tour.save()
        url = reverse('tourlist')
        return url


class DeleteTourView(DeleteView):
    model = Tour
    template_name = 'tourdelete.html'
    success_url = reverse_lazy('tourlist')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'loginform.html', {'form': form})

    def post(self, request):
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            login(request, loginForm.user)
            return redirect("/")
        return render(request, 'loginform.html', {'form': loginForm})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signupform.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['re_password']
            User.objects.create_user(**form.cleaned_data)
            return redirect('/')
        return render(request, 'signupform.html', {'form': form})


class AddReviewView(CreateView):
    model = Review
    fields = '__all__'
    template_name = 'reviewform.html'

    def get_success_url(self):
        review = self.object
        url = reverse('review')
        return url


class ReviewView(ListView):
    def get(self, request):
        reviews = Review.objects.all()
        return render(request, 'reviewlist.html', {'reviews': reviews})


class TourDetails(DetailView):
    model = Tour
    fields = '__all__'
    template_name = 'tourdetails.html'

    def get_success_url(self):
        tour = self.object
        url = reverse('tourdetails', args=(tour.id))
        return url


class ContactView(View):
    def get(self, request):
        form = EmailForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Kontakt z adventuretours"
            imie = cd['imie']
            tekst = cd['tekst']
            send_mail(subject, imie, settings.DEFAULT_FROM_EMAIL, [cd['odbiorca']])
            messageSent = True
        else:
            form = EmailForm()
        return render(request, 'contact.html', {
            'form': form,
            'messageSent': messageSent,

        })


class ReservationView(CreateView):
    model = UserReservation
    fields = '__all__'
    template_name = 'reservationform.html'

    def get_success_url(self):
        url = reverse('reservation')
        return url

class ReservationList(View):
    def get(self, request):
        tour = Tour.objects.all()
        reservation = UserReservation.objects.all()
        return render(request, 'reservationlist.html', {'reservation': reservation, 'tour': tour})


