# Example based in:
# http://stackoverflow.com/questions/20473563/python-qt4-passing-arguments-in-qtcore-qobject-connect
from observer import Observable, Event


class RightButton:
    pass


class LeftButton:
    pass


class MouseEvent(Event):

    def __init__(self):
        self.on(self.handler)

    def __repr__(self):
        return '{} ({},{})'.format(self.button.__name__, self.x, self.y)

    def handler(self, x, y, button):
        self.x = x
        self.y = y
        self.button = button
        print('\tMouse clicked {}'.format(self))


class Label(Observable):

    def __init__(self, name):
        self.name = name
        self.on('click', self.clicked)

    def __repr__(self):
        return self.name

    def clicked(self, e):  # default handler
        print('\tLabel \'{}\' clicked'.format(self))


class Window(Observable):

    def __init__(self, rows, cols):
        self.widgets = [[None for x in range(rows)] for x in range(cols)]
        self.build()

    def __repr__(self):
        return self.__class__.__name__ + ' Window'

    def build(self):  # abstract method to build events, widgets, etc.
        pass

    def widget(self, x, y, widget=None):  # get [or add] a widget
        if widget:
            self.widgets[x][y] = widget
        return self.widgets[x][y]

    def show(self):
        print('Show {} Window:'.format(self.__class__.__name__))
        for row in self.widgets:
            print('\t', ' '.join([str(y or '.') for y in row]))


class Test(Window):

    def build(self):  # template method
        self.on('click', self.clicked)
        self.widget(0, 0, Label('a'))
        self.widget(0, 4, Label('b')).click.on(self.label_clicked)  # add other

    def label_clicked(self, e):
        label = self.widget(e.x, e.y)
        print('\tLabel \'{}\' clicked. Custom handler.'.format(label))

    def clicked(self, e):
        print('\t{} clicked'.format(self))
        self.widget(e.x, e.y).click.trigger(e)


def click_simulator(x, y, btn, window):
    print('Clicking {} at ({},{}) of Window:'.format(btn.__name__, x, y))
    mouse_event = MouseEvent()
    mouse_event.trigger(x, y, btn)
    window.click.trigger(mouse_event)

if __name__ == '__main__':
    test = Test(5, 5)
    test.show()
    click_simulator(0, 0, RightButton, test)
    click_simulator(0, 4, LeftButton, test)

"""
Result:
    Show Test Window:
        a . . . b
        . . . . .
        . . . . .
        . . . . .
        . . . . .
    Clicking RightButton at (0,0) of Window:
        Mouse clicked RightButton (0,0)
        Test Window clicked
        Label 'a' clicked
    Clicking LeftButton at (0,4) of Window:
        Mouse clicked LeftButton (0,4)
        Test Window clicked
        Label 'b' clicked. Custom handler.
        Label 'b' clicked
"""
