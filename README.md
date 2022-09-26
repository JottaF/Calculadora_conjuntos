# Utilizando a classe Conjunto
## Importação
Para utilizar basta importar a classe Conjunto conforme descrito:


```python
from conjunto import Conjunto
```

## Criando um conjunto
Os conjuntos podem ser criados instanciando a classe Conjunto ou como resultado de uma operação, conforme os exemplos:


```python
a = Conjunto()

b = Conjunto()
b.inserir('a', 'b', 'c')

c = Conjunto(1,2,3)

d = Conjunto('a',3,1,'c',2,'b')
```

## Relação entre conjuntos
### Pertinência
*__possui($\mathit{e}$)__*: permite estabelecer se um elemento $\mathit{e}$ pertence a um conjunto $A$. \
*__naoPossui($\mathit{e}$)__*: estabelece a negação da sentença acima


```python
b.possui('b')
```




    True



### Subconjunto
*__contem($A$)__*: permite estabelecer se um conjunto $A$ é subconjunto do conjunto $B$. \
*__naoContem($A$)__*: estabelece a negação da sentença acima.


```python
d.contem(b)
```




    True



### Igualdade
*__igual($B$)__*: permite estabelecer se os conjuntos A e B são iguais, ou seja, se todos os elementos de $A$ também são elementos de $B$.\
*__diferente($B$)__*: estabelece a negação da sentença acima.


```python
e = Conjunto(1,2,3,'a','b','c')
e.igual(d)
```




    True



## Operações entre conjuntos
### Uniao
Retorna um conjunto contendo $A \cup B$


```python
f = b.uniao(c)
f.toString()
```




    '{1,2,3,a,b,c}'



### Interseção
Retorna um conjunto contendo $A \cap B$


```python
e.intersecao(c).toString()
```




    '{1,2,3}'



### Diferença
Retorna um conjunto contendo $A - B$


```python
e.diferenca(c).toString()
```




    '{a,b,c}'



### Conjunto das partes
Retorna um conjunto contendo $2^A$


```python
c.inserir(4)
c.conjuntoDasPartes().toString()
```




    '{{},{1},{2},{3},{4},{1,2},{1,3},{1,4},{2,3},{2,4},{3,4},{1,2,3},{1,2,4},{1,3,4},{2,3,4},{1,2,3,4}}'



### Produto carteziano
Retorna um conjunto contendo $A \cdot B$


```python
c.produtoCartesiano(b).toString()
```




    '{(1,a),(1,b),(1,c),(2,a),(2,b),(2,c),(3,a),(3,b),(3,c),(4,a),(4,b),(4,c)}'



____
# Trechos de códigos
## Relações entre conjuntos
### Pertinência


```python
def possui(self, elemento):
    return str(elemento) in self.toString()
```

### SubConjunto


```python
def contem(self, elemento):
    str1 = self.toString()
    str2 = elemento.toString()
    return str2[1:-1] in str1
```

### Igualdade


```python
def igual(self, elemento):
    return self.toString() == elemento.toString()
```

## Operações entre conjuntos
### União


```python
def uniao(self, elemento):
    uniao = Conjunto()
    for i in self.conjunto:
        uniao.inserir(i)

    if not elemento.conjunto:
        uniao.inserir(Conjunto())
    else:
        for i in elemento.conjunto:
            if not i in uniao.conjunto:
                uniao.inserir(i)

    return uniao
```

### Interseção


```python
def intersecao(self, elemento):
    resultado = Conjunto()
    for i in self.conjunto:
        if i in elemento.conjunto:
            resultado.inserir(i)
        elif type(i) == Conjunto:
            for j in elemento.conjunto:
                if type(j) == Conjunto and j.toString() == i.toString():
                    resultado.inserir(i)
    return resultado
```

### Produto carteziano


```python
def produtoCartesiano(self, elemento):
        coordenadas = Conjunto()
        for i in self.conjunto:
            for j in elemento.conjunto:
                coordenadas.inserir((i, j))
        return coordenadas
```

### Conjunto das partes


```python
def conjuntoDasPartes(self):
    resultado = Conjunto()
    resultado.inserir(Conjunto())

    for i in self.conjunto:
        resultado.inserir(Conjunto(i))

    for i in range(2, len(self.conjunto)+1):
        ponteiros = []

        for j in range(i):
            ponteiros.append(j)

        while ponteiros:
            conjunto = Conjunto()
            for j in ponteiros:
                conjunto.inserir(self.conjunto[j])

            resultado.inserir(conjunto)

            ponteiros = self.__movePonteiros(ponteiros)
    return resultado
```


```python
def __movePonteiros(self, ponteiros: list):
    if ponteiros[-1] != len(self.conjunto)-1:
        ponteiros[-1] += 1
        return ponteiros

    else:
        for i in range(2, len(ponteiros)+1):
            index = len(ponteiros)-i
            if ponteiros[index] == ponteiros[0]:
                if ponteiros[0]+1 != ponteiros[1]:
                    ponteiros[index] += 1
                    for j in range(len(ponteiros)):
                        ponteiros[j] = ponteiros[0]+j
                    return ponteiros

            elif ponteiros[index]+1 != ponteiros[(i-1)*-1]:
                base = ponteiros[index]
                for j in range(index, len(ponteiros)):
                    base += 1
                    ponteiros[j] = base
                return ponteiros

        return []
```

____
#### Repositório:
https://github.com/JottaF/Calculadora_conjuntos




