from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from qrcodeapp.forms import UserForm
from account.models import UserAccount
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            print(user.id)
            return render(request, 'user_detail.html',{'user':user})


    else:
        form = UserForm()
    return render(request, 'user_form.html',{"form":form})
        

def user_detail_view(request, user_id):
    user = get_object_or_404(UserAccount, id=user_id)
    return render(request, 'user_detail.html',{'user':user})

