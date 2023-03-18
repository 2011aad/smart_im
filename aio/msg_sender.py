from channels.layers import get_channel_layer
from django.core.cache import cache


def send_msg(sender, receiver, content):
    receiver_channel_name = cache.get('channel_name_' + receiver)
    get_channel_layer().send(receiver_channel_name, {
        "type": "chat.message",
        "message": content,
    })
    print("message send from " + sender + " to " + receiver + ": " + content)
