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


# Event == Topic
# Observable == Subject == Source == Event Source == Provider
# Observer == Listener == Subscriber

class Window(Observable):
    """
    Para a fonte de eventos Window, tem-se 3 eventos (enviar, receber, click).
    Para cada evento, tem-se apenas um observer que realiza apenas uma acao.
    """

    def subscribe(self, event, subscriber):
        self.on(event, subscriber)

    def publish(self, *args, **kargs):
        return self.trigger(*args, **kargs)

    def tested(self):
        print('tested')

    def buttonenviar(self, a):
        assert(a == '1')

    def buttonreceber(self, a, b, c):
        assert(a == 'a')
        assert(b == 'b')
        assert(c == 2)

    def clicked(self, vai=None):
        print(vai, 'clicked')  # subscriber recebe mensagem (arga)

    def clicked2(self, a, vai=None):
        print(a, vai, 'clicked')  # subscriber recebe mensagem (arga)

    def clicked3(self):
        print('cc')


w = Window()
w.test = Event()
w.events['test'] = w.test
w.test.on(w.tested)
w.test.trigger()
# w.test()
# TODO? descritor para adicionar a test a w.events automaticamente

w.on('test', w.tested)
w.test()

# // Subscribers listen for topics they have subscribed to and
# // invoke a callback function (e.g messageLogger) once a new
# // notification is broadcast on that topic

w.on('enviar', w.buttonenviar)  # subscription
w.on('receber', w.buttonreceber)
w.on('click', w.clicked)  # on: topic - observer/listener
w.subscribe('click2', w.clicked2)
w.subscribe('click3', w.clicked3)
# TODO w.on(['enviar1', 'enviar2'], w.buttonenviar)
# TODO w.on([enviar1, enviar2], w.buttonenviar)

# on(topic, func)
#    Subscribe to events of interest with a specific topic name and a
#     callback function (subscriber), to be executed when the topic/event
#     is observed

# on(topic)
#   gets the topic/event subscriber/handler

# trigger(topic [, args])
#     Publish or broadcast events of interest
#     with a specific topic name and arguments
#     such as the data to pass along


# // Publishers are in charge of publishing topics or notifications of
# // interest to the application.
# publication
w.enviar.trigger('1')  # publica mensagem no evento/topico
w.click.trigger(vai=1)  # publicando mensagem/evento click
# publishing a message under a given topic

print('publishing with trigger ###########################')
w.events['receber'].trigger('a', 'b', 2)
w.trigger('receber', 'a', 'b', 2)
w.publish('receber', 'a', 'b', 2)
w.receber.trigger('a', 'b', 2)

w.events['click'].trigger(vai=1)
w.trigger('click', vai=1)  # publicando mensagem/evento click
w.publish('click', vai=1)  # publicando mensagem/evento click
w.click.trigger(vai=1)

w.events['click2'].trigger(2, vai=3)
w.trigger('click2', 2, vai=3)
w.publish('click2', 2, vai=3)
w.click2.trigger(2, vai=3)

w.events['click3'].trigger()
w.trigger('click3')
w.publish('click3')
w.click3.trigger()
print('end ###########################')


def a(vai=None):
    print('changed', vai)

w.events['click'].on(a)  # add new handler
w.events['click'].trigger(8)
# w.click(vai=1)


class Handler:

    def __call__(self, i, j, a, b):
        assert([i, j, a, b] == [1, 2, 3, 4])


def one_handler(*args, **kargs):
    assert(kargs == {'a': 3, 'b': 4})

two_handler = Handler()  # any callable object can be a handler

subject = Observable()
subject.on('one', one_handler)
subject.on('two', two_handler)
subject.on('many', [one_handler, two_handler])

subject.events['one'].trigger(1, 2, a=3, b=4)  # trigger event one
subject.two.trigger(1, 2, a=3, b=4)  # trigger event two
subject.many(1, 2, a=3, b=4)  # trigger event many

assert(subject.events['one'] == subject.one)
assert(subject.events['two'] == subject.two)
assert(subject.events['many'] == subject.many)
assert(one_handler in subject.one.handlers)
assert(two_handler in subject.two.handlers)
assert(one_handler in subject.many.handlers)
assert(two_handler in subject.many.handlers)

subject.off('many', one_handler)  # remove an handler from the observer events

assert(one_handler not in subject.many.handlers)
assert(two_handler in subject.many.handlers)

subject.off('many')  # remove 'many' event

assert('many' not in subject.events)
try:
    subject.many
    assert(False)
except:
    assert(True)

subject.on('two2', subject.two)  # creating alias for 'two' event
assert(subject.two2 == subject.two)


class ThreeEvent(Event):

    def __init__(self):
        self.on(one_handler)  # add a handler
        self.on(two_handler)  # add another

subject.on('three', ThreeEvent())  # add a subject event with a event object
subject.on('one', ThreeEvent())  # update a subject event with a event object

assert(isinstance(subject.three, ThreeEvent))
assert(ThreeEvent() != ThreeEvent())
"""
"""
