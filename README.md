# Chatting

> `Django`서버에서의 실시간 채팅 서비스입니다.

`WebSocket` 구현을 위해 `Channels` 라이브러리를 사용하였습니다.



- `WebSocket`

  - `http 환경(비연결성, 무상태성)`에서 **양방향 통신**, **실시간 통신**으로 상태를 유지하는 특성을 지녔습니다. 처음엔 `http프로토콜`로 연결되고 이후, `WebSocket`으로 전환되어(이러한 전환을 **`HandShake`**이라고 함) `ws프로토콜`을 사용합니다.

- `Channels`

  - `Django`에서 웹소켓, IoT 프로토콜 등의 프로토콜을 지원하기 위한 라이브러리로 `ASGI`기반으로 개발됨

  - `ASGI`

    - `Django 3.0`부터 지원하는 새로운 기능으로 비동기 웹서버 및 어플리케이션을 만들 수 있도록 함

    - `WSGI(단일 처리만 가능한 동기 호출 방식으로 웹 소켓 연결이나 긴 대기 시간을 갖는 HTTP 연결에 적합하지 않았음)`의 상위 버전

      