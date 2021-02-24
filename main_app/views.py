from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .forms import SendMailForm
from .models import HomePageContent, Product as ProdModel

email = settings.EMAIL_HOST_USER


class Home(ListView):
    model = ProdModel
    template_name = 'main_app/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Home, self).get_context_data(**kwargs)
        ctx['home_content'] = HomePageContent.objects.all().first()
        ctx['form'] = SendMailForm()
        return ctx


class SendMailView(View):
    def post(self, request):
        form = SendMailForm(request.POST)
        if form.is_valid():
            admin = User.objects.filter(is_superuser=True).first()
            subject = "Тестовое задание Максима Загидулина"
            plain_message = "Новое сообщение\n\n" + \
                            "Имя - " + form['name'].value() + "\n" + \
                            "Email - " + form['email'].value()
            from_email = email
            to = admin.email
            # сама функции отправки письма
            send_mail(subject, plain_message, from_email, [to])
        return redirect('home')


class Product(DetailView):
    template_name = 'main_app/product.html'
    model = ProdModel
