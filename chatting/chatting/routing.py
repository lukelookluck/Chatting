from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

# ProtocolTypeRouter가 클라이언트와 Channels 개발 서버가 연결 될 때,
# 어느 프로토콜 타입의 연결인지 확인하고 해당된 미들웨어로 연결해줌
application = ProtocolTypeRouter({
  	# websocket protocol 이라면, AuthMiddlewareStack로 연결
    # AuthMiddlewareStack는 유저가 인증되었는 지에 따라 연결의 범위를 제한해줌
    'websocket': AuthMiddlewareStack(
        # URLRouter에서 넘겨받은 URL을 기반으로 그에 맞는 핸들러를 실행
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})