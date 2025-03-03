
from django.urls import path
from .views import (
    HotelListView, HotelCreateView, HotelUpdateView, HotelDeleteView,
    RoomListView, RoomCreateView, RoomUpdateView, RoomDeleteView,
    EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView,
    home, tologin,tologout
)

urlpatterns = [
    path('', home, name="home1"),
    path('login/', tologin,name="tologin"),
    path('home/', home, name="home"),
    path('logout/', tologout, name="tologout"),


    # Hotel URLs
    path('hotels/', HotelListView.as_view(), name='hotel_list'),
    path('hotels/create/', HotelCreateView.as_view(), name='hotel_create'),
    path('hotels/update/<int:pk>/', HotelUpdateView.as_view(), name='hotel_update'),
    path('hotels/delete/<int:pk>/', HotelDeleteView.as_view(), name='hotel_delete'),

    # Room URLs
    path('rooms/', RoomListView.as_view(), name='room_list'),
    path('rooms/create/', RoomCreateView.as_view(), name='room_create'),
    path('rooms/update/<int:pk>/', RoomUpdateView.as_view(), name='room_update'),
    path('rooms/delete/<int:pk>/', RoomDeleteView.as_view(), name='room_delete'),

    # Employee URLs
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
]