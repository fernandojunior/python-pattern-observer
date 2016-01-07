from observer import Observable

# http://www.dsc.ufcg.edu.br/~jacques/cursos/map/html/arqu/observer.htm
# https://www.safaribooksonline.com/library/view/learning-javascript-design/9781449334840/ch09s05.html
# http://api.jquery.com/trigger/
# http://stackoverflow.com/questions/12627443/jquery-click-vs-onclick
# http://stackoverflow.com/questions/9122078/difference-between-onclick-vs-click
# http://api.jquery.com/trigger/
# http://api.jquery.com/on/
# https://code.jquery.com/jquery-2.1.4.js
# http://stackoverflow.com/questions/15594905/difference-between-observer-pub-sub-and-data-binding
# http://stackoverflow.com/questions/11857325/publisher-subscriber-vs-observer


# TODO: multiplos subscribers por topico
# TODO: mecanismo para parar a propagacao de uma mensagem em topico
#    (.stopPropagation or return False)
# TODO encontrar uma forma de eleminar redundancia em Observable#add
#    self.events[event.name] == event.name + '_'


# Event == Topic
# Observable == Subject == Source == Event Source == Provider
# Observer == Listener == Subscriber == Handler

class Window(Observable):
    """
    Para a fonte de eventos Window, tem-se 3 eventos (enviar, receber, click).
    Para cada evento, tem-se apenas um observer que realiza apenas uma acao.
    """

    def subscribe(self, event, subscriber):
        self.on(event, subscriber)

    def publish(self, *args, **kargs):
        return self.trigger(*args, **kargs)

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



# // Subscribers listen for topics they have subscribed to and
# // invoke a callback function (e.g messageLogger) once a new
# // notification is broadcast on that topic

w.on('enviar', w.buttonenviar)  # subscription
w.on('receber', w.buttonreceber)
w.on('click', w.clicked)  # on: topic - observer/listener
w.subscribe('click2', w.clicked2)
w.subscribe('click3', w.clicked3)

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
w.on('receber')('a', 'b', 2)  # publication
w.enviar('1')  # publica mensagem no evento/topico
w.click(vai=1)  # publicando mensagem/evento click
# publishing a message under a given topic

print('publishing with trigger ###########################')
w.receber_.trigger('a', 'b', 2)
w.trigger('receber', 'a', 'b', 2)
w.publish('receber', 'a', 'b', 2)

w.click_.trigger(vai=1)
w.trigger('click', vai=1)  # publicando mensagem/evento click
w.publish('click', vai=1)  # publicando mensagem/evento click

w.click2_.trigger(2, vai=3)
w.trigger('click2', 2, vai=3)
w.publish('click2', 2, vai=3)

w.click3_.trigger()
w.trigger('click3')
w.publish('click3')
print('end ###########################')


# alterando o subscriber/handler do topico/evento clicked

def a(vai=None):
    print('changed')

w.click_.on(a)
w.click_.trigger()
# w.click(vai=1)

# assert(w.click == w.on('click'))
assert(w.events['click'].call == w.on('click'))
