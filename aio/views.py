from django.shortcuts import render


def index(request):
    return render(request, "aio/index.html")


def chat(request, chat_name):
    return render(request, "aio/chat.html", {"chat_name": chat_name})