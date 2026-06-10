from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_date, parse_time
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Appointment, Doctor
from .permissions import IsStaffUser
from .serializers import StaffTokenObtainPairSerializer


class StaffTokenObtainPairView(TokenObtainPairView):
    serializer_class = StaffTokenObtainPairSerializer


def panel_login(request):
    return render(request, "panel_login.html")


def panel_dashboard(request):
    return render(request, "panel_dashboard.html")


class PanelDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated, IsStaffUser]

    def get(self, request):
        appointments = Appointment.objects.order_by("-created_at")
        doctors = Doctor.objects.order_by("-created_at")

        return Response(
            {
                "user_name": request.user.get_full_name() or request.user.get_username(),
                "stats": {
                    "appointments": appointments.count(),
                    "doctors": doctors.count(),
                    "active_doctors": doctors.filter(is_active=True).count(),
                },
                "appointments": [
                    {
                        "id": item.id,
                        "patient_name": item.patient_name,
                        "email": item.email,
                        "phone": item.phone,
                        "department": item.department,
                        "appointment_date": item.appointment_date,
                        "appointment_time": item.appointment_time,
                        "message": item.message,
                        "created_at": item.created_at,
                    }
                    for item in appointments
                ],
                "doctors": [
                    {
                        "id": item.id,
                        "name": item.name,
                        "specialty": item.specialty,
                        "bio": item.bio,
                        "is_active": item.is_active,
                        "image": item.image.url if item.image else item.image_url,
                    }
                    for item in doctors
                ],
            }
        )


class PanelAppointmentDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsStaffUser]

    def patch(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)

        for field in [
            "patient_name",
            "email",
            "phone",
            "department",
            "appointment_date",
            "appointment_time",
            "message",
        ]:
            value = request.data.get(field)
            if value not in [None, ""]:
                if field == "appointment_date":
                    value = parse_date(value)
                    if value is None:
                        return Response({"detail": "Invalid appointment date."}, status=400)
                if field == "appointment_time":
                    value = parse_time(value)
                    if value is None:
                        return Response({"detail": "Invalid appointment time."}, status=400)
                setattr(appointment, field, value)

        appointment.save()
        return Response({"detail": "Appointment updated successfully."})


class PanelDoctorDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsStaffUser]

    def patch(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)

        for field in ["name", "specialty", "bio", "image_url"]:
            value = request.data.get(field)
            if value not in [None, ""]:
                setattr(doctor, field, value)

        if "is_active" in request.data:
            doctor.is_active = str(request.data.get("is_active")).lower() in ("1", "true", "yes", "on")

        if request.FILES.get("image"):
            doctor.image = request.FILES["image"]

        doctor.save()
        return Response({"detail": "Doctor updated successfully."})
