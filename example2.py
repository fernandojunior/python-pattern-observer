"""
Exemplo utilizando o padrao de projeto Templated Method.
"""

from observer import Event, Observable


class WindowEvent(Event):

    def __init__(self, window):
        Event.__init__(self, self.__class__.__name__.lower())
        self.window = window
        assert(isinstance(self.window, Window))


class Enviar(WindowEvent):

    def call(self, a):
        return a


class Receber(WindowEvent):

    def call(self, a, b, c):
        return a, b, c


class Window(Observable):

    def add(self, event):
        Observable.add(self, event.__class__.__name__.lower(), event.call)

    def __init__(self):
        self.add(Enviar(self))
        self.add(Receber(self))


w = Window()
assert(w.enviar('1') == '1')
assert(w.receber('a', 'b', 2) == ('a', 'b', 2))
