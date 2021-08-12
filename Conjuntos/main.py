from conjunto import Conjunto

a = Conjunto('A')
b = Conjunto('B')
c = Conjunto('C')

a.inserir(2)
a.inserir(1)
a.inserir(5)

a.imprimir()

b.inserir(2)
b.inserir(4)
b.inserir(6)


c.inserir(2)
c.inserir(4)
c.inserir(6)

print(a.uniao(b))

a.imprimir()

print(b.contido(a))
print(b.contido(c))
print(c.contido(b))
