"""
Exemplo utilizando o padrao de projeto Templated Method.
"""

from observer import Event, Observer


class WindowEvent(Event):

    def __init__(self, window):
        Event.__init__(self, self.__class__.__name__.lower())
        self.window = window
        self.window.add(self)


class Enviar(WindowEvent):

    def call(self, a):
        assert(a == '1')


class Receber(WindowEvent):

    def call(self, a, b, c):
        assert(a == 'a')
        assert(b == 'b')
        assert(c == 2)


class Window(Observer):

    def __init__(self):
        self.listeners()

    def listeners(self):
        Enviar(self)
        Receber(self)


w = Window()
w.enviar('1')
w.receber('a', 'b', 2)
