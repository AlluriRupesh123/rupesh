
from django.urls import path
from rupesh.views import list
urlpatterns = [
    path('',list.as_view())

]