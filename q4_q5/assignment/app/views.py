import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import User
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "app/index.html", {
        "user": request.user
    })


def login_view(request):
    if request.method == "POST":

        username = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "app/login.html", {
                "message": "Invalid email or password."
            })
    else:
        return render(request, "app/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        # username = request.POST["username"]
        email = request.POST["email"]

        phone = request.POST["phone"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "app/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user

        try:
            user = User.objects.create_user(
                username=email, email=email, password=password, phone=phone)
            user.save()
        except IntegrityError:
            return render(request, "app/register.html", {
                "message": "Email already registered."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "app/register.html")


@csrf_exempt
def calculate(request):

    def cal(x, n):
        res = 0
        for i in range(1, n+1):
            res += 1/(x**i)
        return res

    data = json.loads(request.body)
    print(data)
    result = cal(data['x'], data['n'])
    return JsonResponse({"result": result}, status=201)
