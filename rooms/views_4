from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import Http404
from . import models


def room_detail(request, pk):
    # print(request)  --> <WSGIRequest: GET '/rooms/66'>
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
        # raise Http404()
