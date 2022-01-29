from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Logged-in User View
@login_required
def profile(request):
    return render(request, "blango_auth/profile.html")