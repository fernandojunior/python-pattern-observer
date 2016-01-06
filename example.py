from observer import Observer


class Window(Observer):
    def __init__(self):
        self.listeners()

    def listeners(self):
        # criando eventos
        self.on('enviar', self.buttonenviar)
        self.on('receber', self.buttonreceber)

    def buttonenviar(self, a):
        assert(a == '1')

    def buttonreceber(self, a, b, c):
        assert(a == 'a')
        assert(b == 'b')
        assert(c == 2)


w = Window()

# acionando eventos
w.enviar('1')
w.on('receber')('a', 'b', 2)
