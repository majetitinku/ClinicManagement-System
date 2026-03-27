from django.db import models


# ================= USER ROLE =================
class User(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('STAFF', 'Staff'),
        ('PATIENT', 'Patient'),
    ]

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


# ================= PATIENT =================
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    disease = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ================= STAFF (Doctor) =================
class Staff(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ================= APPOINTMENT =================
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.patient} - {self.staff}"