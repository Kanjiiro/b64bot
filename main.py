#!/usr/bin/python3
import sys
import time
import telepot
import base64 as b
from telepot.loop import MessageLoop
from telepot.delegate import per_inline_from_id, create_open, pave_event_space

#Use the token you got from fatherbot
TOKEN = ""


class InlineHandler(telepot.helper.InlineUserHandler, telepot.helper.AnswererMixin):
    def __init__(self, *args, **kwargs):
        super(InlineHandler, self).__init__(*args, **kwargs)

    def on_inline_query(self, msg):
        def compute_answer():
            query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
            print(self.id, ':', 'Inline Query:', query_id, from_id, query_string)
            try:
                if "-d" in msg['query']:
                    query_string = b.b64decode(msg['query'].split()[1])
                    bot.sendMessage(from_id,query_string)
                    time.sleep(10)
                else:
                    query_string = str(b.b64encode(query_string.encode()).decode())
            except:
                TypeError
            articles = [{'type': 'article',
                             'id': 'abc', 'title': query_string, 'message_text': query_string}]
            return articles
        self.answerer.answer(msg, compute_answer)

    def on_chosen_inline_result(self, msg):
        from pprint import pprint
        pprint(msg)
        result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
        print(self.id, ':', 'Chosen Inline Result:', result_id, from_id, query_string)



try:
    bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(per_inline_from_id(), create_open, InlineHandler, timeout=10),])
    MessageLoop(bot).run_as_thread()
except:
    TypeError
    socket.timeout
    telepot.exception.TelegramError('Bad Request: message text is empty', 400)
    Exception
print('Listening ...')

while 1:
    time.sleep(10)
