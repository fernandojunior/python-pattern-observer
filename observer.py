"""
Versao 2
Acionamento de um evento permite passagem de argumentos.
Observer armazena apenas um evento por nome.
"""


class Event2(object):

    def __init__(self, name, call=None):
        self.name = name or self.__class__.__name__
        self.call = call or self.call

    def call(self):
        pass


class Observer2(object):

    def __init__(self):
        self.events = {}  # dicionario para armazenar eventos

    def add(self, event):
        """Adiciona um evento"""
        self.events[event.name] = event
        # metodo generico para acionar um evento
        setattr(self, event.name, self.call(event.name))

    def on(self, *args):
        if len(args) == 1:
            return self.call(args[0])
        elif len(args) == 2:
            name = args[0]
            handler = args[1]
            self.add(Event2(name, handler))

    def call(self, name):
        """Metodo que aciona um evento por nome"""
        return self.events[name].call


def f(a):
    assert(a == 1)


def f2(a, b):
    assert(a == 1)
    assert(b == '2')


e = Event2('e', f)
e2 = Event2('e2', f2)

o = Observer2()
o.add(e)
o.add(e2)

# acionando e
e.call(1); o.call('e')(1); o.on('e')(1); o.e(1)

# acionando e2
e2.call(1, '2'); o.call('e2')(1, '2'); o.on('e2')(1, '2'); o.e2(1, '2')
