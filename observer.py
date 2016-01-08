"""
Implementacao do padrao de projeto observer em Python.

Nessa versao, o acionamento de um evento Event#trigger permite passagem de
argumentos e o Observable armazena apenas um observer por evento, o que faz com
que a classe Observer posssa ser abstraida e seu handler (callback) ser
utilizado diretamente.

::author::
    Fernando Felix do Nascimento Junior
::license::
    MIT License
"""


class Event(object):
    """Event or topic"""

    def __init__(self, call=None):
        if call:
            self.on(call)

    def on(self, call):  # [re]binding a subscriber/listener/observer/reciver
        self.__call__ = call                               # handler/callback

    def trigger(self, *args, **kwargs):    # notify/emit a msg to observer
        return self.__call__(*args, **kwargs)     # handler do some action


class Observable(object):
    """Observable or subject or provider or event source/generator"""

    events = {}

    def on(self, event, handler):
        self.events[event] = Event(handler)
        setattr(self, event, self.events[event])  # self.event.trigger()

    def trigger(self, *args, **kargs):
        return self.events[args[0]].trigger(*args[1:], **kargs)
