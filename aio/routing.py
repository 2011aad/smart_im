from django.urls import re_path

from . import ws_handler

websocket_urlpatterns = [
    re_path(r"ws/aio/(?P<chat_name>\w+)/$", ws_handler.AioWsConsumer.as_asgi()),
]