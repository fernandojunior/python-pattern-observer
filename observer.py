"""
Implementacao do padrao de projeto observer em Python.

Nessa versao, o acionamento de um evento Event#call permite passagem de
argumentos e o Observer armazena apenas um evento por nome.

::author::
    Fernando Felix do Nascimento Junior
::license::
    MIT License
"""


class Event(object):  # event or topic

    def __init__(self, name, call=None):
        self.name = name
        self.call = call or self.call  # handler or subscriber or listener or observer

    def on(self, call):
        self.call = call

    def trigger(self, *args, **kwargs):
        return self.call(*args, **kwargs)


class Observable(object):  # observable or subject or provider or event source/generator

    events = {}

    def add(self, event):  # add event listener
        self.events[event.name] = event
        # permite acionar um evento diretamente
        setattr(self, event.name, event.call)
        # permite acessar evento diretamente
        setattr(self, event.name + '_', event)

    def on(self, *args):
        if len(args) == 1:
            return self.events[args[0]].call
        else:
            self.add(Event(*args))

    def trigger(self, *args, **kargs):
        return self.events[args[0]].trigger(*args[1:], **kargs)
