import json

from channels.generic.websocket import WebsocketConsumer

from . import send_message.send_msg


class AioWsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, data):
        json_data = json.loads(data)
        message = json_data["message"]
        print("receive message: " + data)
        print("channel name: " + self.channel_name)
        send_msg(self.channel_name, message["to"], message)
        self.send(text_data = json.dumps({"message": "message sent to " + message["to"] + ": " + message}))

    def chat_message(self, event):
        self.send(text_data = event["message"])