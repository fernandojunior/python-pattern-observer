========
Observer
========

A observer pattern implementation in Python.
--------------------------------------------

The observer pattern is a software design pattern in which an object, called
the subject, maintains a list of its dependents, called observers, and notifies
them automatically of any state changes, usually by calling one of their
methods [#]_.

The **observer.py** implementation has a topic-based system, a message filtering
type of the publish–subscribe pattern (an observer pattern variation) [#]_.
Therefore, a subject can be subdivided into topics and observers can express
interest in one (or more) topic and only receive notifications (with any
message or not) from that.

The implementation is also based on the jquery publish–subscribe model. So, for
convenience, observers will be called **handlers** and topics will be called
**events**. The observer module has only two members: Event and Observable. An
**Observable** instance allows you connect different handlers to its events.
A handler can be any function, method or callable object.

A simpler implementation of the pattern can be found at **observer.old.py**.

Examples
--------

An event with a handler attached:
.. code:: python

    def clicked(a, b, c=None):
        print('clicked ', a, b, c)

    print('A document event (click) with a handler:')
    document = Observable()
    document.on('click', clicked)  # create event dynamically
    document.click(1, 2, c=3)

    # Verbose version:
    document = Observable()
    document.click = Event()
    document.events['click'] = document.click
    document.click.on(clicked)  # add a handler to the event
    document.click.trigger(1, 2, c=3)  # trigger event handler with arguments

An event with many handlers attached:
.. code:: python

    def clicked1():
        print('clicked1.')

    def clicked2():
        print('clicked2.')

    def clicked3():
        print('clicked3.')

    document = Observable()
    document.on('click', [clicked1, clicked2, clicked3])
    document.click.trigger()

    # A version using callable objects:
    class Clicked:

        def __init__(self, i):
            self.msg = 'clicked{}.'.format(i)

        def __call__(self):
            print(self.msg)

    clicked1 = Clicked(1)
    clicked2 = Clicked(2)
    clicked3 = Clicked(3)
    document = Observable()
    document.on('click', [clicked1, clicked2, clicked3])
    document.trigger('click')

Two events that contains the same handlers attached:
.. code:: python

    document = Observable()
    document.on('clicka', [clicked1, clicked2, clicked3])
    document.on('clickb', [clicked1, clicked2, clicked3])

    # simpler:
    document.on(['clicka', 'clickb'], [clicked1, clicked2, clicked3])

    # more simpler:
    document.on('clicka clickb', [clicked1, clicked2, clicked3])

    # trigger two events at once:
    document.trigger(['clicka', 'clickb'])

Add an event with predefined event object that contains many handlers attached:
.. code:: python
    class ClickEvent(Event):

        def __init__(self):
            self.on(self.clicked1)
            self.on(self.clicked2)
            self.on(self.clicked3)

        def clicked1(self):
            print('clicked1.')

        def clicked2(self):
            print('clicked2.')

        def clicked3(self):
            print('clicked3.')

    click_event = ClickEvent()  # predefined event object

    document = Observable()
    document.on('click', click_event)  # add...

    # Replace document event behaviour:
    click_event2 = ClickEvent()  # new event object
    document.on('click', click_event2)  # update ...

    # Two events with same event object reference:
    document.on('click click_alias', click_event)

Add many events with a dictionary:
.. code:: python
    document = Observable()
    document.on({
        'click click_alias': click_event,
        'clicka clickb': [clicked1, clicked2, clicked3],
        'click1': clicked1,
        'click2': clicked2,
        'click3': clicked3})

    # Different ways to trigger event handlers:
    document.click()
    document.clicka.trigger()
    document.clickb.trigger()
    document.trigger(['click1', 'click2', 'click3'])

Synonyms
------------

    - Observer: handler, listener, receiver, consumer, subscriber;
    - Observable: subject, source, provider, generator;
    - Topic: event;
    - Notify: trigger, notify, emit, publish.

Author
------

Fernando Felix do Nascimento Junior.

License
-------

MIT License.

References
----------

.. [#] https://en.wikipedia.org/wiki/Observer_pattern
.. [#] https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern
