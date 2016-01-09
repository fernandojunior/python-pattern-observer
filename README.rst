========
Observer
========

A observer pattern implementation in Python.
--------------------------------------------

The observer pattern is a software design pattern in which an object, called
the subject, maintains a list of its dependents, called observers, and notifies
them automatically of any state changes, usually by calling one of their
methods [#]_.

The *observer.py* implementation has a topic-based system, a message filtering
type of the publish–subscribe pattern (an observer pattern variation) [#]_.
Therefore, a subject can be subdivided into topics and observers can express
interest in one (or more) topic and only receive notifications (with any
message or not) from that. For now, a subject topic can be watched only by an
observer.

A simpler implementation of the pattern can be found at *observer.old.py*.

.. [#] https://en.wikipedia.org/wiki/Observer_pattern
.. [#] https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern

**Synonym list**

    - Observer: listener, receiver, consumer, subscriber.
    - Observable: subject, source, provider, generator.
    - Event:topic.
    - Trigger: notify, emit, publish.
    - Handler: callback, call, __call__


:author:
    Fernando Felix do Nascimento Junior
:license:
    MIT License
