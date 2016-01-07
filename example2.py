"""
Exemplo utilizando o padrao de projeto Templated Method.
"""

from observer import Event, Observable


class WindowEvent(Event):

    def __init__(self, window):
        self.window = window
        assert(isinstance(self.window, Window))


class Enviar(WindowEvent):

    def call(self, a):
        return a


class Receber(WindowEvent):

    def call(self, a, b, c):
        return a, b, c


class Window(Observable):

    def __init__(self):
        self.title = 'Hello World.'
        self.on(Enviar)
        self.on(Receber)

    def on(self, event_class):
        name = event_class.__name__.lower()
        event = event_class(self)
        Observable.on(self, name, event.call)

w = Window()
assert(w.enviar.trigger('1') == '1')
assert(w.receber.trigger('a', 'b', 2) == ('a', 'b', 2))
