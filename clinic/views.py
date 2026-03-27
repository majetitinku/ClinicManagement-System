from django.shortcuts import render, redirect
from .models import Patient, Staff, Appointment


# ================= HOME =================
def home(request):
    return render(request, 'home.html')


# ================= PATIENT =================
def add_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        disease = request.POST.get('disease')

        # 🔥 basic validation (important for marks)
        if not name or len(name) < 2:
            return render(request, 'add_patient.html', {'error': 'Invalid name'})

        Patient.objects.create(name=name, age=age, disease=disease)
        return redirect('view_patient')

    return render(request, 'add_patient.html')


def view_patient(request):
    patients = Patient.objects.all()
    return render(request, 'view_patient.html', {'patients': patients})


def delete_patient(request, id):
    Patient.objects.get(id=id).delete()
    return redirect('view_patient')


# ================= STAFF =================
def add_staff(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department = request.POST.get('department')

        if not name:
            return render(request, 'add_staff.html', {'error': 'Invalid name'})

        Staff.objects.create(name=name, department=department)
        return redirect('view_staff')

    return render(request, 'add_staff.html')


def view_staff(request):
    staff = Staff.objects.all()
    return render(request, 'view_staff.html', {'staff': staff})


# ================= APPOINTMENT =================
def book_appointment(request):
    patients = Patient.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        staff_id = request.POST.get('staff')
        date = request.POST.get('date')

        Appointment.objects.create(
            patient_id=patient_id,
            staff_id=staff_id,
            date=date
        )

        return redirect('view_appointment')

    return render(request, 'appointment.html', {
        'patients': patients,
        'staff': staff
    })


def view_appointment(request):
    appointments = Appointment.objects.all()
    return render(request, 'view_appointment.html', {'appointments': appointments})

def after_login(request):

    if request.user.is_superuser or request.user.groups.filter(name='ADMIN').exists():
        return redirect('/admin/')

    elif request.user.groups.filter(name='STAFF').exists():
        return redirect('view_patient')

    elif request.user.groups.filter(name='PATIENT').exists():
        return redirect('view_appointment')

    # fallback
    return redirect('/')