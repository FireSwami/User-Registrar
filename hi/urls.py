from django.urls import path

from hi.views import already_page, HelloView, VisitorsListView, hello_page

urlpatterns = [
    # path('', index, name='home'),
    path("", HelloView.as_view(), name='home'),
    path("visitors/", VisitorsListView.as_view(), name='visitors'),
    # path('list/', visiter_list, name='list'),
    path('hello/', hello_page, name='hello'),
    # path("hello/", Hello.as_view(), name='hello'),
    path('already/', already_page, name='already'),
]

