from channels.layers import get_channel_layer

def send_msg(sender, receiver, content):
    get_channel_layer().send(receiver, {
        "type": "chat.message",
        "message": content,
    })
    print("message send from " + sender + " to " + receiver + ": " + content)
