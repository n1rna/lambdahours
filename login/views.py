from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import addActivityForm
from login.models import activity
from django.utils.timezone import datetime
import pdb

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating

def home(request):
    return render(request,"home.html")

@login_required(login_url="login/")
def dashboard(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
    context = {
        "user": user
    }
    return render(request,"dashboard.html", context)

@login_required(login_url="login/")
def activities(request):

    user = None
    if request.user.is_authenticated():
        user = request.user

    form = addActivityForm(request.POST or None)
    form_flag = form.is_valid()

    today = datetime.today()
    now = datetime.now()

    if form_flag:
        user.profile.add_activity(form.cleaned_data['comment'],today,now)

    activities = user.profile.activity_set.order_by('-activity_date')

    context = {
        "user": user,
        "flag": form_flag,
        "acts": activities
    }
    return render(request,"activities.html", context)
