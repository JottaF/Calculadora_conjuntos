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
possui(e): permite estabelecer se um elemento e pertence a um conjunto $A$. \
naoPossui(e): estabelece a negação da sentença acima


```python
b.possui('b')
```




    True



### Subconjunto
contem(A): permite estabelecer se um conjunto $A$ é subconjunto do conjunto $B$. \
naoContem(A): estabelece a negação da sentença acima.


```python
d.contem(b)
```




    True



### Igualdade
igual(B): permite estabelecer se os conjuntos $A$ e $B$ são iguais, ou seja, se todos os elementos de $A$ também são elementos de $B$.\
diferente(B): estabelece a negação da sentença acima.


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



