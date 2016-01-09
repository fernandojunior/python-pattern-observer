"""
===============
Observer (old)
===============

::author::
    Fernando Felix do Nascimento Junior
::license::
    MIT License
"""


class Observable(object):

    events = {}  # categorizes observers by event

    def on(self, event, observer):  # observer must be a callable object
        if event not in self.events:
            self.events[event] = []
            setattr(self, event, lambda: self.notify(event))  # self.event()
        self.events[event].append(observer)

    def off(self, event, observer):
        self.events[event].remove(observer)

    def notify(self, event):  # notifies observers by event
        for observer in self.events[event]:
            observer(self)  # observer.__call__(self)

if __name__ == '__main__':
    class Observer:

        def __init__(self):
            self.msg = 'I saw it.'

        def __call__(self, source):  # observer handler
            print(source.count, self.msg)

    def another_observer(source):  # funcitons are callable objects
        print(source.count, "Me too!")

    subject = Observable()
    subject.count = 0
    print('Attach a observer to an event')
    subject.on('hello', Observer())
    subject.count = 1  # changing subject state
    subject.notify('hello')  # notifying observers of hello event
    print('Attach another observer...')
    subject.on('hello', another_observer)
    subject.count = 2
    subject.hello()
    print('Deattach an observer...')
    subject.off('hello', another_observer)
    subject.count = 3
    subject.hello()

    # OUTPUT #
    # Attach a observer to an event
    # 1 I saw it.
    # Attach another observer...
    # 2 I saw it.
    # 2 Me too!
    # Deattach an observer...
    # 3 I saw it.
