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
        self.events = {}  # dicionario para armazenar eventos

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


class Hello(Observer):

    def __init__(self, msg=None):
        self.msg = msg or 'Ai dentro'

    def update(self):
        print(self.msg)

# criando dois observers
hello = Hello()
hello2 = Hello('Papai noel')

# criando objeto observable
obj = Observable()

# anexando observers ao evento hello do objeto a ser observado
obj.add('hello', hello)
obj.add('hello', hello2)

# notifica todos os observers que estao observando o evento hello
obj.hello()  # == obj.notify('hello')
# Result:
#   Ai dentro
#   Papai Noel
