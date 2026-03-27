from django.contrib import admin
from django.urls import path
from clinic import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    # ================= ADMIN =================
    path('admin/', admin.site.urls),
    path('after-login/', views.after_login, name='after_login'),

    # ================= AUTH =================
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    # ================= HOME =================
    path('', views.home, name='home'),

    # ================= PATIENT =================
    path('add-patient/', views.add_patient, name='add_patient'),
    path('view-patient/', views.view_patient, name='view_patient'),
    path('delete-patient/<int:id>/', views.delete_patient, name='delete_patient'),

    # ================= STAFF =================
    path('add-staff/', views.add_staff, name='add_staff'),
    path('view-staff/', views.view_staff, name='view_staff'),

    # ================= APPOINTMENT =================
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('view-appointment/', views.view_appointment, name='view_appointment'),
]