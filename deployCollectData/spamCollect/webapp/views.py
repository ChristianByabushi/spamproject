from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
import csv
from django.contrib.auth import logout
from .forms import SpamMessageForm, contactForm
from .models import Contact, Messages, spamsMessage
# from .serializers import ContactSerializer, spamsMessageSerializer


def index_view(request):
    return render(request, "indexu.html")


def download_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="messages.csv"'

    writer = csv.writer(response)
    writer.writerow(["id", "Contact", "Message"])
    messages = spamsMessage.objects.all().order_by("createat")

    for message in messages:
        writer.writerow(
            [
                message.createat,
                message.contact,
                message.message,
            ]
        )
    return response


def statistic_views(request):
    query_set = spamsMessage.objects.all()
    content_query = request.GET.get("message")
    contact_query = request.GET.get("contact")
    if contact_query:
        query_set = query_set.filter(contact__icontains=content_query)
    if content_query:
        query_set = query_set.filter(message__icontains=content_query)
    paginator = Paginator(query_set, 5)  # paginate by 10 messages per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "messages": page_obj,
        "contact": contact_query,
        "message": content_query,
    }
    return render(request, "statistics.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
        error = "Invalid username or password."
        return render(request, "loginu.html", {"error": error})
    else:
        return render(request, "loginu.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def spamsMessageView(request):
    if request.method == "POST":
        form = SpamMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "success"})
        else:
            return JsonResponse({"error": form.errors})
    else:
        return JsonResponse({"error": "Only POST requests are allowed."})

def contactView(request):
    # def create(self, request: Request, pk=None):
    #     serializer_item = ContactSerializer(data=request.data)
    #     serializer_item.is_valid(raise_exception=True)
    #     serializer_item.save()
    #     return JsonResponse({"message": "success"})
    # return Response(data=serializer_item.data, status=status.HTTP_201_CREATED) 
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "success"})
        else:
            return JsonResponse({"error": form.errors})
    else:
        return JsonResponse({"error": "Only POST requests are allowed."}) 
