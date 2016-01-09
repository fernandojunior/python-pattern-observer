"""
===============
Observer (old)
===============

::author::
    Fernando Felix do Nascimento Junior
::license::
    MIT License
"""


class Observer(object):

    def update(self):  # observer handler
        pass


class Observable(object):

    def __init__(self):
        self.events = {}  # categoriza observers por evento

    def add(self, event, observer):
        """Adiciona um observer a determinado evento."""
        if event not in self.events:
            self.events[event] = []
            setattr(self, event, lambda: self.notify(event))  # self.event()

        self.events[event].append(observer)

    def notify(self, event):
        """Notifica observers por evento."""
        for e in self.events[event]:
            e.update()

if __name__ == '__main__':
    class Hello(Observer):

        def __init__(self, msg):
            self.msg = msg

        def update(self):
            print(self.msg)

    # criando observable
    obj = Observable()
    # criando e anexando observers ao evento hello de obj
    obj.add('hello', Hello('Ai dentro'))
    obj.add('hello', Hello('Papai noel'))
    # notificando observers do evento hello
    obj.hello()  # obj.notify('hello')
    # Result:
    #   Ai dentro
    #   Papai Noel
