# -*- coding: utf-8 -*-


import asyncio
import hangups

import config


@asyncio.coroutine
def sync_recent_conversations(client):
    user_list, conversation_list = (
        yield from hangups.build_user_conversation_list(client)
    )
    all_users = user_list.get_all()
    all_conversations = conversation_list.get_all(include_archived=True)

    # print('{} known users'.format(len(all_users)))
    # for user in all_users:
    #     print('    {}: {}'.format(user.full_name, user.id_.gaia_id))

    print('{} known conversations'.format(len(all_conversations)))
    for conversation in all_conversations:
        if conversation.name:
            name = conversation.name
        else:
            name = 'Unnamed conversation'
        print('{} - {}'.format(name, conversation.id_))



if __name__ == "__main__":
    cookies = hangups.auth.get_auth_stdin(config.REFRESH_TOKEN_PATH)
    client = hangups.Client(cookies)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(sync_recent_conversations(client))
    )
    loop.close()
