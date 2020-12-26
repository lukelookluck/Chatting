# 비동기 방식
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.scope : 각 Consumer 에서 연결정보를 가지고 있는 변수이고, 소켓 통신을 연결한 사용자가 인증된 사용자인지도 검증
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # 해당 채널이 속하는 그룹의 이름을 정해주는 부분
        self.room_group_name = 'chat_%s' % self.room_name

        # 실제로 채널을 그룹에 등록하는 함수
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    # 그룹에서 탈퇴
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # 메세지 수신
    async def receive(self, text_data):
        # 메시지 변수 작성
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # 그룹에 전송
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # 메세지 발신
    async def chat_message(self, event):
        # 메세지 변수 작성
        message = event['message']

        # 웹소켓에 전송
        await self.send(text_data=json.dumps({
            'message': message
        }))





''' 동기 방식
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # "room" 그룹에 가입
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # "room" 그룹에서 탈퇴
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # 웹소켓 으로 부터 메시지 수신
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # "room" 그룹에 메시지 전송
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # "room" 그룹에서 메시지 전송
    def chat_message(self, event):
        message = event['message']

        # 웹 소켓으로 메시지 전송
        self.send(text_data=json.dumps({
            'message': message
        }))
'''