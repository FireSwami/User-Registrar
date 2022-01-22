from django.urls import path

from hi.views import HelloView, VisitorsListView, already_page, hello_page

urlpatterns = [
    path("", HelloView.as_view(), name="home"),
    path("visitors/", VisitorsListView.as_view(), name="visitors"),
    path("hello/", hello_page, name="hello"),
    path("already/", already_page, name="already"),
]
