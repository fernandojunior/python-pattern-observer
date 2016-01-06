# http://www.dsc.ufcg.edu.br/~jacques/cursos/map/html/arqu/observer.htm


class Event():
    def __init__(self, source):
        self.source = source


# Observable
class Telefone():
    observers = []

    # def on(self, event, do):

    def toca(self):
        event = Event(self)
        for o in self.observers:
            o.tocou(event)

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
        telefone.observers.append(Pessoa())
        telefone.observers.append(Secretaria())
        telefone.toca()

App()
