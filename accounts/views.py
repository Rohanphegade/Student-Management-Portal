from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages



# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)   # SESSION CREATED HERE

            if user.is_superuser:
                return redirect('/admin/')
            elif user.groups.filter(name='Manager').exists():
                return redirect('student_list')
            else:
                return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')


    return render(request, 'accounts/login.html')


#  logout
def logout_view(request):
    logout(request)   # session destroyed
    return redirect('login')
