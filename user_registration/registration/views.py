from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
import time

def register_users(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            num_users = form.cleaned_data['num_users']
            start_time = time.time()
            registered_users = [f'User{i+1}' for i in range(num_users)]
            end_time = time.time()
            elapsed_time = end_time - start_time

            messages.success(request, f'Зарегистрировано {num_users} пользователей за {elapsed_time:.2f} секунд!')
            return render(request, 'registration/index.html', {'registered_users': registered_users})

    else:
        form = RegistrationForm()

    return render(request, 'registration/index.html', {'form': form})