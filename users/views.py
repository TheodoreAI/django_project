from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Add to your create your views here.

#i need to post the data here 
# this is used to accept the new info from the login form from the user
def register(request):
    """user creation form in html from django"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # saves the new user to the database
            form.save()
            # getting the username 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! {username} may Login!')
            # sends the user back to the homepage so they can sign in
            return redirect('login')
        else:
            # if the form is not valid
            messages.error(request, f'Account failed to create, please try again!')
            return render(request, 'users/register.html',{'form': form})   
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    """This will make  the  profiles for the users IF they are signed in (using a decorator)"""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            # sends the user to their profile so they can sign in
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request,'users/profile.html', context)
