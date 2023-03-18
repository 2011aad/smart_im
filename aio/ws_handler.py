import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.core.cache import cache

from . import msg_sender


class AioWsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        json_data = json.loads(text_data)
        print("receive message: " + text_data)

        if 'method' in json_data:
            if json_data['method'] == 'set_user':
                self.set_user(json_data['user'])
                return

        print("channel name: " + self.channel_name)
        async_to_sync(msg_sender.send_msg)(self.channel_name, json_data["to"], json_data["message"])
        self.send(text_data = json.dumps({"message": "message sent to " + json_data["to"] + ": " + json_data["message"]}))

    def set_user(self, user):
        cache.set('channel_name_' + user, self.channel_name)

    def chat_message(self, event):
        self.send(text_data = event["message"])