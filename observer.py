"""
Implementacao do padrao de projeto observer em Python.

Nessa versao, o acionamento de um evento Event#call permite passagem de
argumentos e o Observer armazena apenas um evento por nome.

::author::
    Fernando Felix do Nascimento Junior
::license::
    MIT License
"""


class Event(object):

    def __init__(self, name, call=None):
        self.name = name
        self.call = call or self.call


class Observer(object):

    events = {}

    def add(self, event):
        """Adiciona um evento"""
        self.events[event.name] = event
        # metodo generico para acionar um evento
        setattr(self, event.name, event.call)

    def on(self, *args):
        if len(args) == 1:
            return self.events[args[0]].call
            # return self.call(args[0])
        else:
            self.add(Event(*args))
