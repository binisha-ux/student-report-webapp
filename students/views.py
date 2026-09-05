from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
 

# Create your views here.

def home(request):
    return render(request, 'home.html')




def add_students(request):
    if request.method == "POST":
        
        data = request.POST


        roll_no = data.get('roll_no')
        student_name = data.get('student_name')
        student_age = data.get('student_age')
        student_email = data.get('student_email')

        Student.objects.create(
            roll_no = roll_no,
            student_name = student_name,
            student_age = student_age,
            student_email = student_email
        )

        return redirect('add_student')

    context = {'page': 'add_new_students'}

    return render(request, 'report_card.html', context)


def student_list(request):
    student = Student.objects.all()

    context = {'students': students}


    return render(request, 'student_list.html', context)
        




def login_page(request):
    if request.method == "POST":
        data = request.POST

        username = data.get('username')
        password = data.get('password')

        user = authenticate(
            request,
            username = username,
            password = password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, 'login.html')









