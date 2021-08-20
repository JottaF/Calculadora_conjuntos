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
print(b.contem(a))
print(b.contem(c))
print(c.contem(b))

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

print('\n\nContido propriamente')
print(a.contidoPropriamente(b))

print('Conjunto das partes')
print(a.conjuntoDasPartes())