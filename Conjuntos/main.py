from conjunto import Conjunto
from universo import Universo

u = Universo()

a = Conjunto()
a.nomear('A')
b = Conjunto()
b.nomear('B')
c = Conjunto()
c.nomear('C')

a.inserir(2)
a.inserir(1)
a.inserir(3)
a.inserir(4)
a.inserir(5)
# a.inserir(6)

b.inserir(2)
b.inserir(4)
b.inserir(6)


c.inserir(6)
c.inserir(2)
c.inserir(4)

print('União')
print(a.uniao(b))

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

print('\nDiferença')
e = a.diferenca(b)
e.nomear('E')

print('\n\nContido propriamente')
print(a.contidoPropriamente(b))

print('\n\nConjunto das partes')
# a.conjuntoDasPartes()
x = Conjunto('x','y','z','a')
x.conjuntoDasPartes()

print('\n\ntoString')
l = Conjunto(1,2,3)
k = Conjunto(1,l)
j = Conjunto()
z = Conjunto(l,k,j)
print(z.toString())

print('\n\nPoduto cartesiano')
p = x.produto_cartesiano(a)
print(p.toString())

print('\n\nt')
t = a.uniao(b).uniao(c)
print(t.toString())

print('\n\nUniverso')
u.getElementos()
# print(u.toString())
