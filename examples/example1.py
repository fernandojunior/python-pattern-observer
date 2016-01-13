# Examples just for test
from observer import Observable, Event


class Handler:

    def __call__(self, i, j, a, b):
        assert([i, j, a, b] == [1, 2, 3, 4])


def one_handler(*args, **kargs):
    assert(kargs == {'a': 3, 'b': 4})

two_handler = Handler()  # any callable object can be a handler
three_handler = Handler()

subject = Observable()
subject.on('one', one_handler)
subject.on('two', two_handler)
subject.on('three', three_handler)
subject.on('many', [one_handler, two_handler])  # event with handlers
subject.many.on(three_handler)  # add another handler
assert(subject.events['one'] is subject.one)
assert(subject.events['two'] is subject.two)
assert(subject.events['three'] is subject.three)
assert(subject.events['many'] is subject.many)
assert(one_handler in subject.one.handlers)
assert(two_handler in subject.two.handlers)
assert(one_handler in subject.many.handlers)
assert(two_handler in subject.many.handlers)
assert(three_handler in subject.many.handlers)

subject.events['one'].trigger(1, 2, a=3, b=4)  # trigger an event with message
subject.two.trigger(1, 2, a=3, b=4)  # trigger ...
subject.many(1, 2, a=3, b=4)  # trigger ...
subject.trigger('one', 1, 2, a=3, b=4)  # trigger ...
subject.trigger(['two', 'many'], 1, 2, a=3, b=4)  # trigger ...

subject.off('many', one_handler)  # remove an handler from subject event
subject.many.off(two_handler)  # remove ...
assert(one_handler not in subject.many.handlers)
assert(two_handler not in subject.many.handlers)

subject.off('many')  # remove an event from subject
assert('many' not in subject.events)
try:
    subject.many
except:
    assert(True)

subject.on('two2', subject.two)  # creating alias for the event
assert(subject.two2 == subject.two)


class ThreeEvent(Event):

    def __init__(self):
        self.on(one_handler)  # add a handler
        self.on(two_handler)  # add another

subject.on('three', ThreeEvent())  # add a subject event with a event object
assert(isinstance(subject.three, ThreeEvent))
assert(one_handler in subject.three.handlers)
assert(two_handler in subject.three.handlers)

subject.on('one', ThreeEvent())  # update a existing event with a event object
assert(ThreeEvent() != ThreeEvent())

subject = Observable()
subject.on({  # setting events of an observable with dictionary
    'one': one_handler,
    'two': two_handler,
    'three': ThreeEvent(),
    'many': [one_handler, two_handler]})

subject = Observable()
subject.on(['two', 'two2'], two_handler)  # events with same handler
assert(subject.two is not subject.two2)
assert(two_handler in subject.two.handlers)
assert(two_handler in subject.two2.handlers)

subject = Observable()
subject.on('many many2', [one_handler, two_handler])  # with same handlers
assert(subject.many is not subject.many2)
assert(one_handler in subject.many.handlers)
assert(two_handler in subject.many.handlers)
assert(one_handler in subject.many2.handlers)
assert(two_handler in subject.many2.handlers)

subject = Observable()
three_event = ThreeEvent()
subject.on(['three', 'three_alias'], three_event)  # events with same reference
assert(three_event is subject.three)
assert(subject.three is subject.three_alias)
subject.trigger('three three_alias', 1, 2, a=3, b=4)


class NotCallable:
    pass

subject = Observable()
try:
    subject.on('error', NotCallable())  # handler must be callable
except:
    assert(True)


# TODO: mecanismo para parar a propagacao de uma mensagem em topico
#    (.stopPropagation or return False)
# TODO? permitir que um evento faca link de outros eventos e.on(e2).on(e3)
# TODO? permitir event namespaces? http://api.jquery.com/on/#event-names
# TODO? subject.trigger(event)
# TODO? document.trigger('click mouseenter')
# TODO? descritor para adicionar a event a w.events automaticamente
