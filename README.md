# Chatting

> `Django`서버에서의 실시간 채팅 서비스입니다.

`WebSocket` 구현을 위해 `Channels` 라이브러리를 사용하였습니다.



- `WebSocket`

  - `http 환경(비연결성, 무상태성)`에서 연결 상태를 계속 유지하기에는 데이터 오버헤드`(응답으로 헤더정보가 같이 오기 때문에 불필요한 더미 트래픽이 발생함)` 문제로 비효율적이고, `keep-alive` 속성이 있지만, 권장되지 않음`(기본적으로 off되어있고 2시간 간격으로 작동되며, 종단[어플리케이션]간 연결이 아님)`
  - `ajax`로 연결 상태를 계속 유지할 수는 있지만, 편법에 불가함`(일정시간 마다 업데이트 or 대기 후 응답이 오면 다시 접속을 위한 코드 실행[대기 - 응답 - 코드 실행 - 대기 - 응답 - 코드 실행 ~])`, 데이터의 오버헤드·과부하 문제`(응답으로 헤더정보가 같이 오기 때문에 불필요한 더미 트래픽이 발생함)`
  - **양방향 통신**, **실시간 통신**으로 상태를 유지하는 특성을 지녔습니다. 처음엔 `http프로토콜`로 연결되고 이후, `WebSocket`으로 전환되어(이러한 전환을 **`HandShake`**이라고 함) `ws프로토콜`을 사용합니다
  - 채팅서버나 푸시알림, 게임 등에 많이 쓰임

- `Channels`

  - `Django`에서 웹소켓, IoT 프로토콜 등의 프로토콜을 지원하기 위한 라이브러리로 `ASGI`기반으로 개발됨
- `ASGI`
  
  - `Django 3.0`부터 지원하는 새로운 기능으로 비동기 웹서버 및 어플리케이션을 만들 수 있도록 함
  - `WSGI(단일 처리만 가능한 동기 호출 방식으로 웹 소켓 연결이나 긴 대기 시간을 갖는 HTTP 연결에 적합하지 않았음)`의 상위 버전
- `Channel Layer`
- 각 Cunsumer끼리 데이터 공유를 위한 것
  - `channel`
    - 데이터를 보낼 통로, 우편함
  - `group`
    - `channel`을 여러개 묶어서 관리하는 단위
  - 백업 저장소
    - 메모리, `radis`, `AMQP`





## 이슈

channels_layer을 생성하기 위해 `pip install channels_redis `를 하고 테스트를 진행한 결과, 

```
File "C:\Users\Luke\AppData\Local\Programs\Python\Python37\lib\site-packages\channels_redis\core.py", line 361, 
in _brpop_with_clean
    result = await connection.bzpopmin(channel, timeout=timeout)
aioredis.errors.ReplyError: ERR unknown command 'BZPOPMIN'
```

와 같은 문제가 발생하였다.

구글링을 해본 결과, `redis`와 `channels-redis`와의 호환성 문제였고 `channels-redis`를 2.4.2 버전으로 설치하여 문제를 해결하였다.