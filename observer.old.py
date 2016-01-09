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

    def add(self, event, observer):  # observer must be a callable object
        if event not in self.events:
            self.events[event] = []
            setattr(self, event, lambda: self.notify(event))  # self.event()
        self.events[event].append(observer)

    def notify(self, event):  # notifies observers by event
        for observer in self.events[event]:
            observer(self)  # observer.__call__(self)

if __name__ == '__main__':
    class HelloObserver:

        def __init__(self):
            self.msg = 'Papai noel'

        def __call__(self, source):  # observer handler
            print(source.count, self.msg)
            source.count += 1

    def another_observer(source):  # funcitons are callable objects
        print(source.count, "Ai dentro")
        source.count += 1

    subject = Observable()
    # Attaching observers to hello event of subject
    subject.add('hello', HelloObserver())
    subject.add('hello', another_observer)
    # changing subject state
    subject.count = 0
    # notifing observers
    subject.hello()  # obj.notify('hello')
    # Result:
    #   0 Ai dentro
    #   1 Papai Noel
