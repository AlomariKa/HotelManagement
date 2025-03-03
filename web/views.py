# hotel/views.py
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Hotel, Room, Employee
from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request,'home.html')

# Hotel Views
class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel/hotel_list.html'
    context_object_name = 'hotels'

class HotelCreateView(LoginRequiredMixin,CreateView):
    model = Hotel
    template_name = 'hotel/hotel_form.html'
    fields = ['name', 'location', 'rating']
    success_url = reverse_lazy('hotel_list')
    # URL resolution needs to be delayed until it is actually needed. Unlike the reverse function, which resolves a URL immediately, reverse_lazy postpones the resolution
class HotelUpdateView(LoginRequiredMixin, UpdateView):
    model = Hotel
    template_name = 'hotel/hotel_form.html'
    fields = ['name', 'location', 'rating']
    success_url = reverse_lazy('hotel_list')

class HotelDeleteView(LoginRequiredMixin, DeleteView):
    model = Hotel
    template_name = 'hotel/hotel_confirm_delete.html'
    success_url = reverse_lazy('hotel_list')
    context_object_name = "hotel"

# Room Views
class RoomListView(ListView):
    model = Room
    template_name = 'room/room_list.html'
    context_object_name = 'rooms'


class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    template_name = 'room/room_form.html'
    fields = ['hotel', 'room_number', 'room_type', 'price']
    success_url = reverse_lazy('room_list')

class RoomUpdateView(LoginRequiredMixin,UpdateView):
    model = Room
    template_name = 'room/room_form.html'
    fields = ['hotel', 'room_number', 'room_type', 'price']
    success_url = reverse_lazy('room_list')

class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    template_name = 'room/room_confirm_delete.html'
    success_url = reverse_lazy('room_list')
    context_object_name = "room"


# Employee Views
class EmployeeListView(LoginRequiredMixin,ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'


class EmployeeCreateView(LoginRequiredMixin,CreateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    fields = ['hotel', 'name', 'position', 'salary']
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(LoginRequiredMixin,UpdateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    fields = ['hotel', 'name', 'position', 'salary']
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(LoginRequiredMixin,DeleteView):
    model = Employee
    template_name = 'employee/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')
    context_object_name = "employee"

def tologin(request ):
    if request.method == "POST":
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            username = loginform.cleaned_data['user']
            password = loginform.cleaned_data['password']
            # authentication for the users in admin
            user = authenticate(request,username=username,password = password)
            if user is not None: # Check if authentication was successful
                login(request,user)
                return redirect('home')
            else:
                return render(request, 'loginform.html', {})

    else:
        loginform = LoginForm()

    return render(request,'loginform.html',{})


def tologout(request):
    logout(request)
    return render(request,'loginform.html',{})