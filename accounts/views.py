from django.shortcuts import render
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.
def signup(request):
    if re
    form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
