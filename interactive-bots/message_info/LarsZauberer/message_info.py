# See readme.md for instructions on running this code.

from typing import Any

class MessageInfoHandler(object):
    def usage(self) -> str:
        return '''
        This bot will allow users to analyze a message for word count. The gathered information will then be sent to a private conversation with the user. Users should @-mention the bot in the beginning of a message.
        '''

    def handle_message(self, message: Any, bot_handler: Any) -> None:
        words_in_message = message['content'].split()
        content = "You sent a message with {} words.".format(len(words_in_message))
        original_sender = message['sender_email']
        bot_handler.send_message(dict(
            type='private',
            to=original_sender,
            content=content,
        ))

handler_class = MessageInfoHandler
