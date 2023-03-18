from django.shortcuts import render


def chat(request, chat_name):
    return render(request, "aio/chat.html", {"chat_name": chat_name})