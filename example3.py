# http://www.dsc.ufcg.edu.br/~jacques/cursos/map/html/arqu/observer.htm


class Event():

    def __init__(self, source):
        self.source = source  # fonte do evento

    def call(self, name):  # aciona observers para este evento
        for o in self.source.observers:
            getattr(o, name)(self)


# Observable
class Telefone():
    events = {}  # Observable possui lista de eventos
    observers = []

    def __init__(self):
        self.events['toca'] = Event(self)
        # self.events['atende'] = Event(self)

    def on(self, event_name, action_name):
        def f():
            event = self.events[event_name]
            event.call(action_name)

        setattr(self, event_name, f)

    def atende(self):
        event = Event(self)
        for o in self.observers:
            o.atendido(event)


# Observer
class Pessoa():

    def tocou(self, event):
        print('Pessoa escutou..')

    def atendido(self, event):
        print('Pessoa atendeu.')


class Secretaria():

    def tocou(self, event):
        print('Secretaria nao escutou..')

    def atendido(self, event):
        print('Secretaria atendeu.')


class App():

    def __init__(self):
        telefone = Telefone()
        telefone.on('toca', 'tocou')
        telefone.observers.append(Pessoa())
        telefone.observers.append(Secretaria())
        telefone.toca()

App()
