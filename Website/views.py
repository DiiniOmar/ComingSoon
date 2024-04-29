from django.shortcuts import render, redirect
from Website.forms import signUpForm
from Website.models import SignUp
from django.contrib import messages



def SignUpView(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have signed up successfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error with your form. Please correct the errors and try again.")
    else:
        form = signUpForm()
    
    return render(request, 'Website/home.html', {'form': form})

