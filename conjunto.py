import string


class Conjunto:
    def __init__(self, *arg):
        self.conjunto = []

        for i in arg:
            if i not in self.conjunto:
                self.conjunto.append(i)

    def inserir(self, *elemento):
        for i in elemento:
            if i not in self.conjunto:
                self.conjunto.append(i)
            else:
                print('Já possui o elemento ', elemento)
    
    def remover(self, elemento):
        if type(elemento) == Conjunto:
            str1 = elemento.toString()
            for i in self.conjunto:
                if type(i) == Conjunto() and i.toString() == str1:
                    self.conjunto.remove(i)
        else:
            self.conjunto.remove(elemento)

    def tamanho(self):
        return len(self.conjunto)

    def possui(self, elemento):
        return str(elemento) in self.toString()

    def naoPossui(self, elemento):
        return not self.possui(elemento)

    def contem(self, elemento):
        str1 = self.toString()
        str2 = elemento.toString()
        return str2[1:-1] in str1

    def naoContem(self, elemento):
        return not self.contem(elemento)

    def igual(self, elemento):
        return self.toString() == elemento.toString()

    def diferente(self, elemento):
        return not self.igual(elemento)

    def eVazio(self):
        return self.conjunto == []

    def contidoPropriamente(self, elemento):
        str1 = self.toString()
        str2 = elemento.toString()

        return len(str1) < len(str2) and str1[1:-1] in str2

    def naoContidoPropriamente(self, elemento):
        return not self.contidoPropriamente(elemento)

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

    def diferenca(self, elemento):
        resultado = Conjunto()
        for i in self.conjunto:
            if i not in elemento.conjunto:
                resultado.inserir(i)
            elif type(i) == Conjunto:
                for j in elemento.conjunto:
                    if type(j) == Conjunto and j.toString() != i.toString():
                        resultado.inserir(i)

        return resultado

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

    def produtoCartesiano(self, elemento):
        coordenadas = Conjunto()
        for i in self.conjunto:
            for j in elemento.conjunto:
                coordenadas.inserir((i, j))
        return coordenadas

    def toString(self):
        inteiro = []
        string = []
        tupla = []
        conjunto = []

        for i in self.conjunto:
            if type(i) == int:
                inteiro.append(i)
            elif type(i) == str:
                string.append(i)
            elif type(i) == tuple:
                tupla.append(i)
            elif type(i) == Conjunto:
                conjunto.append(i.toString())

        inteiro.sort()
        inteiro += sorted(string)
        inteiro += sorted(tupla)
        inteiro += conjunto

        resultado = '{'
        for i in range(len(inteiro)):
            if type(inteiro[i]) == type(Conjunto()):
                resultado += inteiro[i].toString()
            elif type(inteiro[i]) == tuple:
                resultado += self.__toStringTupla(inteiro[i])
            else:
                resultado += (str(inteiro[i]))

            if i < len(inteiro) - 1:
                resultado += ','

        return resultado + '}'

    def __toStringTupla(self, tupla):
        resultado = '('
        for i in range(len(tupla)):
            if type(tupla[i]) == type(Conjunto()):
                resultado += tupla[i].toString()
            elif type(tupla[i]) == tuple:
                resultado += self.__toStringTupla(tupla[i])
            else:
                resultado += str(tupla[i])

            if i < len(tupla) - 1:
                resultado += ','

        return resultado + ')'
