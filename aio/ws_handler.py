import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from . import msg_sender


class AioWsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        json_data = json.loads(text_data)
        message = json_data["message"]
        print("receive message: " + text_data)
        print("channel name: " + self.channel_name)
        async_to_sync(msg_sender.send_msg)(self.channel_name, message["to"], message)
        self.send(text_data = json.dumps({"message": "message sent to " + message["to"] + ": " + message}))

    def chat_message(self, event):
        self.send(text_data = event["message"])