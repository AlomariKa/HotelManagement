# hotel/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Hotel, Room, Employee
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

# Hotel Views
class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel/hotel_list.html'
    context_object_name = 'hotels'

class HotelCreateView(CreateView):
    model = Hotel
    template_name = 'hotel/hotel_form.html'
    fields = ['name', 'location', 'rating']
    success_url = reverse_lazy('hotel_list')
    # URL resolution needs to be delayed until it is actually needed. Unlike the reverse function, which resolves a URL immediately, reverse_lazy postpones the resolution
class HotelUpdateView(UpdateView):
    model = Hotel
    template_name = 'hotel/hotel_form.html'
    fields = ['name', 'location', 'rating']
    success_url = reverse_lazy('hotel_list')

class HotelDeleteView(DeleteView):
    model = Hotel
    template_name = 'hotel/hotel_confirm_delete.html'
    success_url = reverse_lazy('hotel_list')
    context_object_name = "hotel"

# Room Views
class RoomListView(ListView):
    model = Room
    template_name = 'room/room_list.html'
    context_object_name = 'rooms'


class RoomCreateView(CreateView):
    model = Room
    template_name = 'room/room_form.html'
    fields = ['hotel', 'room_number', 'room_type', 'price']
    success_url = reverse_lazy('room_list')

class RoomUpdateView(UpdateView):
    model = Room
    template_name = 'room/room_form.html'
    fields = ['hotel', 'room_number', 'room_type', 'price']
    success_url = reverse_lazy('room_list')

class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'room/room_confirm_delete.html'
    success_url = reverse_lazy('room_list')
    context_object_name = "room"


# Employee Views
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    fields = ['hotel', 'name', 'position', 'salary']
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    fields = ['hotel', 'name', 'position', 'salary']
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')
    context_object_name = "employee"
