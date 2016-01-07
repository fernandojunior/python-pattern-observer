from observer import Observer


# https://www.safaribooksonline.com/library/view/learning-javascript-design/9781449334840/ch09s05.html
# http://api.jquery.com/trigger/
# http://stackoverflow.com/questions/12627443/jquery-click-vs-onclick
# http://stackoverflow.com/questions/9122078/difference-between-onclick-vs-click
# http://api.jquery.com/trigger/
# http://api.jquery.com/on/

Provider = Observer


# Observable == Subject == Source == Event Source == Publisher
# Observer == Listener == Subscriber

class Window(Provider):
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


# on(topic, func)
#    // Subscribe to events of interest
#     // with a specific topic name and a
#     // callback function, to be executed
#     // when the topic/event is observed

# // Subscribers listen for topics they have subscribed to and
# // invoke a callback function (e.g messageLogger) once a new
# // notification is broadcast on that topic

w.on('enviar', w.buttonenviar)  # subscription
w.on('receber', w.buttonreceber)
w.on('click', w.clicked)  # on: topic - observer/listener
w.subscribe('click2', w.clicked2)
w.subscribe('click3', w.clicked3)


# on(topic)
# gets the topic/event subscriber/handler

# on(topic)(args)
# // Publish or broadcast events of interest
#  // with a specific topic name and arguments
#  // such as the data to pass along

# // Publishers are in charge of publishing topics or notifications of
# // interest to the application.
w.on('receber')('a', 'b', 2)  # publication
w.enviar('1')  # publica mensagem no evento/topico
w.click(vai=1)  # publicando mensagem/evento click

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
