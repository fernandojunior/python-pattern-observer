# tests ...
from pytest import raises
from observer import Observable, Event


class CustomEvent(Event):

    def __init__(self):
        self.on(one_handler)  # add a handler
        self.on(two_handler)  # add another


class NotCallable:
    pass


class Handler:

    def __call__(self, i, j, a, b):
        assert([i, j, a, b] == [1, 2, 3, 4])


def one_handler(*args, **kargs):
    assert(kargs == {'a': 3, 'b': 4})

two_handler = Handler()  # any callable object can be a handler
three_handler = Handler()


def test_event_with_handler_attached():
    subject = Observable()
    subject.on('one', one_handler)
    subject.on('two', two_handler)
    assert(subject.events['one'] is subject.one)
    assert(subject.events['two'] is subject.two)
    # trigger
    subject.one(1, 2, a=3, b=4)
    subject.one.trigger(1, 2, a=3, b=4)
    subject.trigger('one', 1, 2, a=3, b=4)
    subject.events['one'].trigger(1, 2, a=3, b=4)
    subject.trigger('one two', 1, 2, a=3, b=4)
    subject.trigger(['one', 'two'], 1, 2, a=3, b=4)


def test_event_with_many_handlers_attached():
    subject = Observable()
    subject.on('many', [one_handler, two_handler])
    assert(subject.events['many'] is subject.many)
    assert(one_handler and two_handler in subject.many.handlers)
    # remove a handler
    subject.off('many', one_handler)
    assert(one_handler not in subject.many.handlers)
    # remove the event
    subject.off('many')
    assert('many' not in subject.events)
    with raises(AttributeError):
        subject.many


def test_custom_event():
    subject = Observable()
    custom_event = CustomEvent()
    subject.on('custom', custom_event)
    subject.on(['custom', 'custom_alias'], custom_event)  # same reference
    assert(subject.custom and subject.custom_alias is custom_event)
    assert(one_handler and two_handler in subject.custom.handlers)
    # update an event
    subject.on('custom', CustomEvent())
    assert(subject.custom is not custom_event)


def test_events_with_same_handler_attached():
    subject = Observable()
    subject.on(['one', 'one2'], one_handler)
    assert(subject.one is not subject.one2)
    assert(one_handler in subject.one.handlers)
    assert(one_handler in subject.one2.handlers)


def test_events_with_same_handlers_attached():
    subject = Observable()
    subject.on('many many2', [one_handler, two_handler])
    assert(subject.many is not subject.many2)
    assert(one_handler and two_handler in subject.many.handlers)
    assert(one_handler and two_handler in subject.many2.handlers)


def test_many_events_with_dictionary():
    subject = Observable()
    subject.on({  # setting events of an observable with dictionary
        'one': one_handler,
        'two': two_handler,
        'custom': CustomEvent(),
        'many': [one_handler, two_handler]})
    subject.trigger('one two custom many', 1, 2, a=3, b=4)


def test_no_callable_handler():
    subject = Observable()
    with raises(TypeError):
        subject.on('error', NotCallable())

"""
TODO: mecanismo para parar a propagacao de uma mensagem em topico
    (.stopPropagation or return False)
TODO? permitir que um evento faca link de outros eventos e.on(e2).on(e3)
TODO? permitir event namespaces? http://api.jquery.com/on/#event-names
TODO? subject.trigger(event)
TODO? thread safe
    http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Observer.html
"""
