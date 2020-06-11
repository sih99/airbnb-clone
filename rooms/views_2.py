from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):

    page = request.GET.get("page", 1)
    # page = request.GET.get("page")
    # /?page=  ---> ""
    # /  ---> "None"
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    # rooms = paginator.page(int(page))
    # rooms -----> <Page 2 of 5>
    # rooms = paginator.get_page(page)
    # rooms  ---- > <Page 5 of 5> <Page 1 of 5>..
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"rooms": rooms})
    except EmptyPage:
        return redirect("/")
