from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views import View
from django.views.generic import DeleteView, UpdateView, ListView

from Tours_app.forms import LoginForm, SignUpForm
from Tours_app.models import Tour


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
        return render(request, 'tourlist.html', {'objects': tours})


class TourDetails(View):
    def get(self, request):
        return render(request, 'tourdetails.html')

#
#
# class AddTourView(View):
#     def get(self, request):
#         tour_id = request.GET.get('id')
#         if tour_id is not None:
#             tour = Tour.objects.get(id=tour_id)
#         else:
#             tour = None
#         return render(request, 'form.html', {'tour_name': tour})
#
#     def post(self, request):
#         tour_name = request.POST.get('tour_name')
#         tour_days = request.POST.get('tour_days')
#         tour_type = request.POST.get('tour_type')
#         tour_country = request.POST.get('tour_country')
#
#         t = Tour.objects.create(tour_name=tour_name, tour_days=tour_days, tour_type=tour_type,
#                                 tour_country=tour_country)
#         url = reverse('tourlist')
#         return redirect(url)
#
# class UpdateTourView(UpdateView):
#     model = Tour
#     fields = '__all__'
#     template_name = 'form.html'
#
#     def get_success_url(self):
#         tour = self.object
#         url = reverse('tourdetails', args=(tour.id,))
#         return url
#
#
# class DeleteTourView(DeleteView):
#     model = Tour
#     template_name = 'delete.html'
#     success_url = reverse_lazy('tourlist')


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
