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

    def on(self, event, call=None):
        """Add/Reset an event or create new one with an handler attached."""
        if isinstance(call, Event):  # add an event or reset it, if exists
            self.events[event] = call
        elif event in self.events:  # add new handler to an event
            self.events[event].on(call)
        else:  # create new event
            self.events[event] = Event(call)
        setattr(self, event, self.events[event])  # self.event.trigger()

    def trigger(self, *args, **kargs):
        """
        Execute the observer with message for an event of this observable.
        """
        return self.events[args[0]].trigger(*args[1:], **kargs)
