from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect

from django.urls import reverse

from django.contrib.auth import logout, login, authenticate

from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Log the user out."""
    logout(request)
    return redirect('learning_logs:index')

def register(request):
    """Register a new method"""
    if request.method != 'POST':
        #display blank registration form.
        form = UserCreationForm()
    else:
        #Process complated Form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
            #log the user in and then redirect to home page.
            #authenticated_user = authenticate(username=new_user.username, passward=request.POST['passward1'])
            login(request, authenticated_user)
            return redirect('learning_logs:index')


    context = {'form': form}
    return render(request, 'registration/register.html', context)
    import pdb
    pdb.set_trace()

