"""
========
Observer
========

An observer pattern implementation in Python based on jQuery.

:author:
    Fernando Felix do Nascimento Junior
:license:
    MIT License
"""


class Event(object):
    """An event that handlers can express interest in."""

    def __init__(self, handler=None):
        if handler:
            self.on(handler)

    def __call__(self, *args, **kwargs):
        """Execute all event handlers using obj.trigger() or just obj()."""
        return self.trigger(*args, **kwargs)

    @property
    def handlers(self):
        """Return all event handlers."""
        if not hasattr(self, '_handlers'):  # avoid call __init__ in subclasses
            self._handlers = set()
        return self._handlers

    def on(self, handler):
        """Attach a handler (any Python callable) for the event."""
        if not hasattr(handler, '__call__'):
            raise TypeError('handler is not a callable object.')
        self.handlers.add(handler)

    def off(self, handler):
        """Deattach a handler for the event."""
        self.handlers.remove(handler)

    def trigger(self, *args, **kwargs):
        """Execute the handlers with a message, if any."""
        for h in self.handlers:
            h(*args, **kwargs)


class Observable(object):
    """A object to be observed. It can be subdivided into many events."""

    @property
    def events(self):
        """Return all events of the observable."""
        if not hasattr(self, '_events'):
            self._events = {}
        return self._events

    def on(self, event, handler=None):
        """Create, add or update an event with a handler or more attached."""
        if isinstance(event, str) and ' ' in event:  # event is list str-based
            self.on(event.split(' '), handler)
        elif isinstance(event, list):  # many events contains same handler
            for each in event:
                self.on(each, handler)
        elif isinstance(event, dict):  # event is a dict of <event, handler>
            for key, value in event.items():
                self.on(key, value)
        elif isinstance(handler, list):  # handler is a list of handlers
            for each in handler:
                self.on(event, each)
        elif isinstance(handler, Event):  # handler is Event object
            self.events[event] = handler  # add or update an event
            setattr(self, event, self.events[event])  # self.event.trigger()
        elif event in self.events:  # add a handler to an existing event
            self.events[event].on(handler)
        else:  # create new event with a handler attached
            self.on(event, Event(handler))

    def off(self, event, handler=None):
        """Remove an event or a handler from it."""
        if handler:
            self.events[event].off(handler)
        else:
            del self.events[event]
            delattr(self, event)

    def trigger(self, *args, **kargs):
        """
        Execute all event handlers with optional arguments for the observable.
        """
        event = args[0]

        if isinstance(event, str) and ' ' in event:
            event = event.split(' ')  # split event names ...

        if isinstance(event, list):  # event is a list of events
            for each in event:
                self.events[each].trigger(*args[1:], **kargs)
        else:
            self.events[event].trigger(*args[1:], **kargs)
