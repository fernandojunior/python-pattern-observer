from observer import Observable, Event

# http://www.dsc.ufcg.edu.br/~jacques/cursos/map/html/arqu/observer.htm
# https://www.safaribooksonline.com/library/view/learning-javascript-design/9781449334840/ch09s05.html
# http://api.jquery.com/trigger/
# http://api.jquery.com/trigger/
# http://api.jquery.com/on/
# https://code.jquery.com/jquery-2.1.4.js
# http://stackoverflow.com/questions/12627443/jquery-click-vs-onclick
# http://stackoverflow.com/questions/9122078/difference-between-onclick-vs-click
# http://stackoverflow.com/questions/15594905/difference-between-observer-pub-sub-and-data-binding
# http://stackoverflow.com/questions/11857325/publisher-subscriber-vs-observer
# http://stackoverflow.com/questions/8065305/whats-the-difference-between-on-and-live-or-bind
# http://www.javaworld.com/article/2077444/learn-java/speaking-on-the-observer-pattern.html
# http://c2.com/cgi/wiki?SoftwareDesignPatternsIndex

# TODO: multiplos subscribers/listeners por topico/evento Observable#add
# TODO: mecanismo para parar a propagacao de uma mensagem em topico
#    (.stopPropagation or return False)
# TODO? permitir que um evento faca link de outros eventos e.on(e2).on(e3)
# TODO? permitir event namespaces? http://api.jquery.com/on/#event-names
# TODO? subject.trigger(event)


def clicked(a, b, c=None):
    print('clicked ', a, b, c)


def clicked1():
    print('clicked1.')


def clicked2():
    print('clicked2.')


def clicked3():
    print('clicked3.')

print('A document event (click) with a handler:')
document = Observable()
document.click = Event()
document.click.on(clicked)  # add a handler to the event
document.click.trigger(1, 2, c=3)  # trigger event handler with arguments

print('A document event (click) with a handler:')
document = Observable()
document.on('click', clicked)  # create event dynamically
document.click.trigger(1, 2, c=3)

print('A document event (click) with many handlers:')
document = Observable()
document.click = Event()
document.click.on(clicked1)  # add a handler to the event
document.click.on(clicked2)  # add another
document.click.on(clicked3)  # ...
document.click.trigger()  # trigger all event handlers

print('A document event (click) with many handlers:')
document = Observable()
document.on('click', [clicked1, clicked2, clicked3])  # create it dynamically
document.click.trigger()


class Clicked:

    def __init__(self, i):
        self.msg = 'Clicked{}.'.format(i)

    def __call__(self):
        print(self.msg)

print('A document event (click) with many handlers:')
clicked1 = Clicked(1)
clicked2 = Clicked(2)
clicked3 = Clicked(3)
document = Observable()
document.on('click', [clicked1, clicked2, clicked3])
document.trigger('click')

print('Three document events each one with its handler:')
document = Observable()
document.on({
    'click1': clicked1,
    'click2': clicked2,
    'click3': clicked3})
document.click1.trigger()  # different ways to trigger an event
document.click2()
document.trigger('click3')
print('Trigger many events at once:')
document.trigger(['click1', 'click2', 'click3'])  # trigger many events at once

print('Two document events that contains the same handlers:')
document = Observable()
document.on('clicka', [clicked1, clicked2, clicked3])
document.on('clickb', [clicked1, clicked2, clicked3])
document.trigger(['clicka', 'clickb'])

print('Two document events that contains the same handlers:')
document = Observable()
document.on(['clicka', 'clickb'], [clicked1, clicked2, clicked3])
document.trigger(['clicka', 'clickb'])

print('Two document events that contains the same handlers:')
document = Observable()
document.on('clicka clickb', [clicked1, clicked2, clicked3])
document.trigger(['clicka', 'clickb'])


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

print('Add an event with predefined event object that contains many handlers attached:')
click_event = ClickEvent()
click_event2 = ClickEvent()
document = Observable()
document.on('click', click_event)  # create document event with event instance
document.on('click', click_event2)  # replace document event behaviour
document.on('click click_alias', click_event)  # events have the same reference
document.trigger(['click', 'click_alias'])

print('Create many document events with a dictionary:')
document = Observable()
document.on({
    'click click_alias': click_event,
    'clicka clickb': [clicked1, clicked2, clicked3],
    'click1': clicked1,
    'click2': clicked2,
    'click3': clicked3})
document.click()
document.clicka.trigger()
document.clickb.trigger()
document.trigger(['click1', 'click2', 'click3'])

# TODO? document.trigger('click mouseenter')
# TODO? descritor para adicionar a test a w.events automaticamente


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

subject.off('many', one_handler)  # remove an handler from subject event
subject.many.off(two_handler)  # remove ...
assert(one_handler not in subject.many.handlers)
assert(two_handler not in subject.many.handlers)

subject.off('many')  # remove an event from subject
assert('many' not in subject.events)
try:
    subject.many
    assert(False)
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
subject.on(['many', 'many2'], [one_handler, two_handler])  # with same handlers
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
