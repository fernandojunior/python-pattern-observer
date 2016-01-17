========
Observer
========

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
        :target: https://github.com/fernandojunior/observer/blob/master/LICENSE.rst

.. image:: http://img.shields.io/pypi/v/pattern-observer.svg
        :target: https://pypi.python.org/pypi/pattern-observer

.. image:: https://img.shields.io/pypi/status/pattern-observer.svg
        :target: https://pypi.python.org/pypi/pattern-observer

.. image:: https://img.shields.io/travis/fernandojunior/python-pattern-observer.svg
        :target: https://travis-ci.org/fernandojunior/python-pattern-observer

.. image:: https://img.shields.io/codecov/c/github/fernandojunior/python-pattern-observer.svg
        :target: https://codecov.io/github/fernandojunior/python-pattern-observer

The observer pattern is a software design pattern in which an object, called
the subject, maintains a list of its dependents, called observers, and notifies
them automatically of any state changes, usually by calling one of their
methods [#]_.

The **observer.py** implementation has a topic-based system, a message filtering
type of the publish–subscribe pattern (an observer pattern variation) [#]_.
Therefore, a subject can be subdivided into topics and observers can express
interest in one (or more) topic and only receive notifications (with any
message or not) from that.

The implementation is also based on the jquery publish–subscribe model [#]_
[#]_. So, for convenience, observers will be called **handlers** and topics
will be called **events**. The observer module has only two members: Event and
Observable. An **Observable** instance allows you connect different handlers to
its events. A handler can be any function, method or callable object.

A simpler implementation of the pattern can be found at **old.py**.

Installation
------------

.. code-block:: bash

    $ pip install pattern-observer

Alternatively, download the source **observer.py** and put it in the root
directory of your project.

Examples/Features
-----------------

An event with a handler attached:

.. code:: python

    from observer import Event, Observable

    def clicked(a, b, c=None):
        print('clicked ', a, b, c)

    document = Observable()
    document.on('click', clicked)  # create event dynamically with a handler attached
    document.click(1, 2, c=3)  # notify event handler with arguments

    # Verbose version:
    document = Observable()
    document.click = Event()  # create event
    document.events['click'] = document.click  # add it to the dict of events
    document.click.on(clicked)  # atach a handler to the event
    document.click.trigger(1, 2, c=3)  # notify the handler ...

    document.off('click')  # remove an event

    # Output:
    # clicked  1 2 3

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

        def __call__(self):  # make it callable
            print(self.msg)

    clicked1 = Clicked(1)
    clicked2 = Clicked(2)
    clicked3 = Clicked(3)
    document = Observable()
    document.on('click', [clicked1, clicked2, clicked3])
    document.trigger('click')

    document.off('click', clicked1)  # remove a handler from the event

    # Output:
    # clicked3.
    # clicked2.
    # clicked1.

Two events that contains the same handlers attached:

.. code:: python

    document = Observable()
    document.on('clicka', [clicked1, clicked2, clicked3])
    document.on('clickb', [clicked1, clicked2, clicked3])

    # Simpler:
    document.on(['clicka', 'clickb'], [clicked1, clicked2, clicked3])

    # More simpler:
    document.on('clicka clickb', [clicked1, clicked2, clicked3])

    # Trigger two events at once:
    document.trigger(['clicka', 'clickb'])  # or
    document.trigger('clicka clickb')

    # Output:
    # clicked1.
    # clicked3.
    # clicked2.
    # clicked1.
    # clicked3.
    # clicked2.


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
    document.on('click', click_event)  # add new entry with predefined obj ...

    # Replace event behaviour:
    click_event2 = ClickEvent()  # new event object
    document.on('click', click_event2)  # update the entry with new obj ...

    # Two events can point same event object reference:
    document.on('click click_alias', click_event)

    # Trigger
    document.trigger(['click', 'click_alias'])

    # Output:
    # clicked1.
    # clicked2.
    # clicked3.
    # clicked1.
    # clicked2.
    # clicked3.

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

    # Output:
    # ...

Contributing
------------

If you're making changes, check that your changes pass flake8 and the tests,
including testing other Python versions with tox:

.. code-block:: bash

    $ flake8 observer.py tests.py
    $ python -m tests.py
    $ tox

To get flake8 and tox, just pip install them into your virtualenv.

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.6, 2.7, 3.3, 3.4 and 3.5. Check
   https://travis-ci.org/fernandojunior/python-pattern-observer/pull_requests
   and make sure that the tests pass for all supported Python versions.


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

Released under MIT License.

References
----------

.. [#] https://en.wikipedia.org/wiki/Observer_pattern
.. [#] https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern
.. [#] http://api.jquery.com/trigger/
.. [#] http://api.jquery.com/on/

Links
-----

- http://c2.com/cgi/wiki?SoftwareDesignPatternsIndex
- https://www.safaribooksonline.com/library/view/learning-javascript-design/9781449334840/ch09s05.html
- http://stackoverflow.com/questions/15594905/difference-between-observer-pub-sub-and-data-binding
- http://stackoverflow.com/questions/8065305/whats-the-difference-between-on-and-live-or-bind
- http://stackoverflow.com/questions/11857325/publisher-subscriber-vs-observer
- http://www.javaworld.com/article/2077444/learn-java/speaking-on-the-observer-pattern.html
