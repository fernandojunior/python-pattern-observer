from observer import Event, Observer


def f(a):
    assert(a == 1)


def f2(a, b):
    assert(a == 1)
    assert(b == '2')


e = Event('e', f)
e2 = Event('e2', f2)

o = Observer()
o.add(e)  # publica o evento 'e'
o.on('e2', f2)  # cria um evento 'e2' dinamicamente e o publica

# acionando 'e'
e.call(1)
o.call('e')(1)
o.on('e')(1)
o.e(1)

# acionando 'e2'
o.call('e2')(1, '2')
o.on('e2')(1, '2')
o.e2(1, '2')
