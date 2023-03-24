from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm


# Create your views here.

def register(request):
    if request.method=='POST': # trying to input data, called once signup is clicked
        form=RegisterForm(request.POST) # request.POST in brackets means data is being sent to the user creation form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # extracts the username from the cleaned data, just form data but all the inputs are separate
            messages.success(request, f'welcome {username}, your account is created')
            return redirect('login')
    else: # called before the if condition
        form = RegisterForm()
        return render(request, 'users/register.html', {'form':form}) # the {{form}} in register.html
            




