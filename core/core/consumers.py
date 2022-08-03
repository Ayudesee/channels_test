# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def connect(self):
        # Logic to add all groups to User websocket
        self.channel_name = self.scope['user']
        user = self.scope['user']
        print(f"{user = }")
        # if user.is_anonymous:
        #     self.close()

        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name = f'user_{self.user_id}'

        print(self.room_group_name)
        print(f"{self.channel_name = }")
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # # Receive message from WebSocket
    # def receive(self, text_data):
    #     print("in receive")
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #
    #     # Send message to room group
    #     async_to_sync(self.channel_layer.group_send)(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )

    # Receive message from room group
    def chat_message(self, event):
        print("in chat_message")
        print(f"{event = }")
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'event': 'tack_added',
            'message': message
        }))

    def tack_add(self, event):
        print(f"{event = }")
        message = event['message']

        async_to_sync(self.channel_layer.group_add)(
            f"tacker_{message['tacker']}",
            self.channel_name
        )
