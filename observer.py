__author__ = 'Fernando Felix do Nascimento Junior'
__license__ = 'MIT'

class Event(object):
    __name__ = None # opcional

    def action(self): # aciona o evento
        pass

class Observer(object):

    def __init__(self):
        self.events = {}  # dicionario para armazenar eventos

    def add(self, event):
        """Adiciona um evento"""

        event_name = event.__name__ or event.__class__.__name__

        # se não existe uma lista de eventos com determinado nome ...
        if event_name not in self.events:
            self.events[event_name] = []

        self.events[event_name].append(event)

        # criando metodo dinamicamente para acionar eventos de um determinado nome
        setattr(self, event_name, lambda: self.action(event_name))

    def action(self, name):
        """Metodo que aciona uma lista de eventos (por nome)"""
        for e in self.events[name]:
            e.action()
            
class Hello(Event):
    __name__ = 'hello'

    def __init__(self):
        self.msg = 'Ai dentro'

    def action(self):
        print(self.msg)

# criando dois eventos
hello = Hello()
hello2 = Hello()

hello2.msg = 'Papai noel'

# criando observer
obj = Observer()
obj.add(hello)
obj.add(hello2)

# aciona os eventos de nome hello
obj.hello() # ou obj.action('hello')
# Ai dentro
# Papai Noel