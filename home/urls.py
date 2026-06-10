from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import panel, views


urlpatterns = [

    path('', views.index, name='home'),

    path('about/', views.about, name='about'),

    path('booking/', views.booking, name='booking'),

    path('appointments/',
    views.appointments,
    name='appointments'),

    path('update/<int:id>/',
    views.update,
    name='update'),

    path('delete/<int:id>/',
    views.delete,
    name='delete'),

    path('doctors/',
    views.doctors,
    name='doctors'),

    path('contact/',
    views.contact,
    name='contact'),

    path('services/',
    views.services,
    name='services'),

    path('panel/login/', panel.panel_login, name='panel_login'),

    path('panel/', panel.panel_dashboard, name='panel_dashboard'),

    path('panel/api/dashboard/', panel.PanelDashboardAPIView.as_view(), name='panel_dashboard_api'),

    path('panel/api/appointments/<int:pk>/', panel.PanelAppointmentDetailAPIView.as_view(), name='panel_appointment_detail'),

    path('panel/api/doctors/<int:pk>/', panel.PanelDoctorDetailAPIView.as_view(), name='panel_doctor_detail'),

    path('panel/api/token/', panel.StaffTokenObtainPairView.as_view(), name='panel_token'),

    path('panel/api/token/refresh/', TokenRefreshView.as_view(), name='panel_token_refresh'),

]
