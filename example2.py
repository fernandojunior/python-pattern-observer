"""
Exemplo utilizando o padrao de projeto Templated Method.
"""

from observer import Event, Observable


class WindowEvent(Event):

    def __init__(self, window):
        self.window = window
        assert(isinstance(self.window, Window))


class Enviar(WindowEvent):

    def __call__(self, a):
        return a


class Receber(WindowEvent):

    def __call__(self, a, b, c):
        return a, b, c


class Window(Observable):

    def __init__(self):
        self.title = 'Hello World.'
        self.receber = Receber(self)
        self.enviar = Enviar(self)
        self.on('receber2', self.receber)  # criando alias
        # self.receberAli = self.receber

w = Window()
assert(w.enviar.trigger('1') == '1')
assert(w.receber.trigger('a', 'b', 2) == ('a', 'b', 2))
assert(w.receber2.trigger('a', 'b', 2) == ('a', 'b', 2))
assert(w.trigger('receber2', 'a', 'b', 2) == ('a', 'b', 2))
assert(w.receber == w.receber2)
