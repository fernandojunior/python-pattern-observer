# Exemplo para acoplar o observable ao evento.
# É utilizando o padrao de projeto Templated Method.
from observer import Event, Observable


class WindowEvent(Event):

    def __init__(self, window):
        assert(isinstance(window, Window))
        self.window = window
        self.on(self.handler)

    def handler(self):  # teamplte method
        pass


class Enviar(WindowEvent):

    def handler(self, a):
        assert(isinstance(self.window, Window))
        assert(a == '1')
        print('enviar was called')


class Receber(WindowEvent):

    def handler(self, *args):
        print('receber was called ', args)


class Receber2(WindowEvent):

    def handler(self, *args):
        assert(isinstance(self.window, Window))
        print('receber2 was called ', args)


class Window(Observable):

    def __init__(self):
        self.title = 'Hello World.'

        print('Create and trigger enviar event:')
        self.on('enviar', Enviar(self))
        self.enviar.trigger('1')

        print('Create and trigger receber event:')
        self.receber = Receber(self)
        self.receber.trigger('a', 'b', 2)

        print('Replace and trigger receber event:')
        self.on('receber', Receber2(self))  # replace all event behaviour
        self.receber.trigger('a', 'b', 2)

        print('Create alias from receber event and trigger it:')
        self.on('receber2', self.events['receber'])  # receber2 == receber
        self.receber2.trigger('a', 'b', 2)
        assert(self.events['receber'] == self.events['receber2'])

        def receber3(*args):
            print('receber3 was called ', args)

        print('Add new handler to receber event:')
        self.on('receber', receber3)  # add new handler to the event
        self.receber2.trigger('a', 'b', 2)

w = Window()
