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
    """An event that an observer can express interest in."""

    def __init__(self, call=None):
        if call:
            self.on(call)

    def on(self, call):
        """Attach an observer (any Python callable) for this event."""
        self.__call__ = call

    def trigger(self, *args, **kwargs):
        """Execute the observer handler with a message, if any."""
        return self.__call__(*args, **kwargs)


class Observable(object):
    """A object to be observed. It can be subdivided into many events."""

    events = {}

    def on(self, event, call=None):
        """Add an event or create an event with an observer attached."""
        self.events[event] = call if isinstance(call, Event) else Event(call)
        setattr(self, event, self.events[event])  # self.event.trigger()

    def trigger(self, *args, **kargs):
        """
        Execute the observer with message for an event of this observable.
        """
        return self.events[args[0]].trigger(*args[1:], **kargs)
