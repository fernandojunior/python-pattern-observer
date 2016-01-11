"""
========
Observer
========

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
        """Create, add or update an event with an handler or more attached."""
        if isinstance(handler, list):  # it's a list of handlers
            for each in handler:
                self.on(event, each)
        elif isinstance(handler, Event):  # add or update an event
            self.events[event] = handler
            setattr(self, event, self.events[event])  # self.event.trigger()
        elif event in self.events:  # add an handler to an existing event
            self.events[event].on(handler)
        else:  # create new event with a handler attached
            self.on(event, Event(handler))

    def off(self, event, handler=None):
        """Remove an event or an handler from it."""
        if handler:
            self.events[event].off(handler)
        else:
            del self.events[event]
            delattr(self, event)

    def trigger(self, *args, **kargs):
        """
        Execute the observer with message for an event of this observable.
        """
        return self.events[args[0]].trigger(*args[1:], **kargs)
