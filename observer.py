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
        self.call = call  # subscriber/listener/observer handler/callback

    def on(self, call):
        self.call = call

    def trigger(self, *args, **kwargs):  # notify the observer to some action
        return self.call(*args, **kwargs)


class Observable(object):
    """Observable or subject or provider or event source/generator"""

    events = {}

    def add(self, name, handler):  # add event listener (just the handler)
        event = Event(handler)
        self.events[name] = event
        setattr(self, name, event.trigger)  # event trigger: self.event()

    def on(self, *args):
        if len(args) == 1:
            return self.events[args[0]].call
        else:
            self.add(*args)

    def trigger(self, *args, **kargs):
        return self.events[args[0]].trigger(*args[1:], **kargs)
