from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages

from .forms import *
from .models import *

def index(request):
    if request.method == 'POST':
        form = SMTPForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['context'],
                form.cleaned_data['email'],
                ['avtandilkgg@gmail.com'],
                fail_silently=False
            )
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('/')
        else:
            messages.error(request, 'Письмо не отправлено')
    else:
        form = SMTPForm()
    return render(request, 'app/index.html', {'form': form})
