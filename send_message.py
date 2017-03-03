# -*- coding: utf-8 -*-


import asyncio
import hangups

import config


@asyncio.coroutine
def send_message(client, conversation_id, message_text):
    request = hangups.hangouts_pb2.SendChatMessageRequest(
        request_header=client.get_request_header(),
        event_request_header=hangups.hangouts_pb2.EventRequestHeader(
            conversation_id=hangups.hangouts_pb2.ConversationId(
                id=conversation_id
            ),
            client_generated_id=client.get_client_generated_id(),
        ),
        message_content=hangups.hangouts_pb2.MessageContent(
            segment=[
                hangups.ChatMessageSegment(message_text).serialize()
            ],
        ),
    )
    yield from client.send_chat_message(request)



if __name__ == "__main__":
    cookies = hangups.auth.get_auth_stdin(config.REFRESH_TOKEN_PATH)
    client = hangups.Client(cookies)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(send_message(client, config.CONVERSATION_ID, "It works"))
    )
    loop.close()
