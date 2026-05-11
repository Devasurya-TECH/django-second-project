from django.shortcuts import get_object_or_404, redirect, render
from .models import Appointment, Doctor


# HOME PAGE

def index(request):

    doctors_list = Doctor.objects.filter(is_active=True).order_by("-created_at")

    return render(
        request,
        "index.html",
        {"doctors": doctors_list}
    )


# ABOUT PAGE

def about(request):

    return render(request, "about.html")


# BOOK APPOINTMENT (CREATE)

def booking(request):

    if request.method == "POST":

        patient_name = request.POST.get('patient_name')

        email = request.POST.get('email')

        phone = request.POST.get('phone')

        department = request.POST.get('department')

        appointment_date = request.POST.get('appointment_date')

        appointment_time = request.POST.get('appointment_time')

        message = request.POST.get('message')

        Appointment.objects.create(

            patient_name=patient_name,

            email=email,

            phone=phone,

            department=department,

            appointment_date=appointment_date,

            appointment_time=appointment_time,

            message=message

        )

        return redirect('appointments')

    return render(request, 'booking.html')


# READ APPOINTMENTS

def appointments(request):

    data = Appointment.objects.order_by("-created_at")

    return render(

        request,

        'appointments.html',

        {'data': data}

    )


# UPDATE APPOINTMENT

def update(request, id):

    appointment = get_object_or_404(Appointment, id=id)

    if request.method == "POST":

        appointment.patient_name = request.POST.get('patient_name')

        appointment.email = request.POST.get('email')

        appointment.phone = request.POST.get('phone')

        appointment.department = request.POST.get('department')

        appointment.appointment_date = request.POST.get('appointment_date')

        appointment.appointment_time = request.POST.get('appointment_time')

        appointment.message = request.POST.get('message')

        appointment.save()

        return redirect('appointments')

    return render(

        request,

        'update.html',

        {'appointment': appointment}

    )


# DELETE APPOINTMENT

def delete(request, id):

    appointment = get_object_or_404(Appointment, id=id)

    if request.method == "POST":
        appointment.delete()

    return redirect('appointments')


# DOCTORS PAGE

def doctors(request):

    doctors_list = Doctor.objects.filter(is_active=True).order_by("-created_at")

    return render(
        request,
        "doctors.html",
        {"doctors": doctors_list}
    )


# CONTACT PAGE

def contact(request):

    return render(request, "contact.html")


# SERVICES PAGE

def services(request):

    return render(request, "services.html")
