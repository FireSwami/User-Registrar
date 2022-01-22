import urllib.parse

from django.shortcuts import redirect, render, reverse
from django.views.generic import FormView, ListView

from hi.forms import HelloForm
from hi.models import Visitors


class HelloView(FormView):
    template_name = "hi/index.html"
    form_class = HelloForm
    success_url = "/hello/"
    extra_context = {"title": "Страница регистрации"}

    def form_invalid(self, form):
        self.request.session["user_data"] = form.cleaned_data
        return redirect(
            reverse("already") + "?" + urllib.parse.urlencode(form.cleaned_data)
        )

    def form_valid(self, form):
        self.request.session["user_data"] = form.cleaned_data
        Visitors.objects.create(**form.cleaned_data)
        return redirect(
            reverse("hello") + "?" + urllib.parse.urlencode(form.cleaned_data)
        )


class VisitorsListView(ListView):
    queryset = Visitors.objects.order_by("time_registration", "last_name")
    template_name = "hi/visitors.html"
    success_url = "/visitors/"
    context_object_name = "visitors"
    extra_context = {"title": "Список посетителей"}


def hello_page(request):
    return render(
        request,
        "hi/hello.html",
        {"user_data": request.session["user_data"], "title": "Страница приветствия"},
    )


def already_page(request):
    return render(
        request,
        "hi/already.html",
        {"user_data": request.session["user_data"], "title": "Страница уведомления"},
    )
