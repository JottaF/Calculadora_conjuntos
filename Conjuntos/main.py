from conjunto import Conjunto

a = Conjunto()
a.nomear('A')
b = Conjunto()
b.nomear('B')
c = Conjunto()
c.nomear('C')

a.inserir(2)
a.inserir(1)
a.inserir(5)
a.inserir(6)

a.imprimir()

b.inserir(2)
b.inserir(4)
b.inserir(6)


c.inserir(6)
c.inserir(2)
c.inserir(4)

print('União')
print(a.uniao(b))

a.imprimir()

print('\nContido')
print(b.contido(a))
print(b.contido(c))
print(c.contido(b))

print('\nIgual')
print(c.igual(b))
print(a.igual(c))
print(b.igual(c))

print('\nConjunto D')
d = a.interseccao(c)
d.nomear('D')
d.inserir(5)
d.imprimir()

print('\nDiferença')
e = a.diferenca(b)
e.nomear('E')
e.imprimir()

print(a.conjuntoDasPartes())