class Conjunto:
    def __init__(self, *arg):
        self.conjunto = []
        self.nome = 'nome'

        for i in arg:
            if i not in self.conjunto:
                self.conjunto.append(i)

    def nomear(self, nome):
        self.nome = nome
    
    def inserir(self, elemento):
        if elemento not in self.conjunto:
            self.conjunto.append(elemento)
        else:
            print('Já possui o elemento ', elemento)
    
    def tamanho(self):
        print(len(self.conjunto))
        
    def possui(self, elemento):
        return elemento in self.conjunto

    def contem(self, elemento):
        for i in self.conjunto:
            if i not in elemento.conjunto:
                return False

        return True
    
    def uniao(self, elemento):
        uniao = Conjunto()
        for i in self.conjunto:
            uniao.inserir(i)

        for i in elemento.conjunto:
            if not i in uniao.conjunto:
                uniao.inserir(i)
        
        return uniao
    
    def igual(self, elemento):
        if len(self.conjunto) == len(elemento.conjunto):
            for i in self.conjunto:
                if i not in elemento.conjunto:
                    return False
        else:
            return False
        return True

    def interseccao(self, elemento):
        result = Conjunto()
        for i in self.conjunto:
            if i in elemento.conjunto:
                result.inserir(i)
        
        return result
    
    def diferenca(self, elemento):
        result = Conjunto()
        for i in self.conjunto:
            if i not in elemento.conjunto:
                result.inserir(i)

        return result
    
    def conjuntoDasPartes(self):
        base = sorted(self.conjunto)
        conjunto = []
        conjunto.append([])

        for i in range(len(base)+1):
            elemento = self.__Rec(base,base,i,i)
            for i in elemento:
                if not i in conjunto:
                    conjunto.append(i)

        print(conjunto)
        return conjunto
    
    def __Rec(self, base, rBase, size,rSize,points=[], times = 0):
        result = []
        for i in range(len(base)):
            if len(base) > 2 and size > 1:
                c = base[i:]
                if not base[i] in points and base[i] != base[-1] and len(points) < rSize:
                    points.append(base[i])
                time = times+1
                result += self.__Rec(c,rBase,size-1,rSize,points,time)

            else:
                lista = points.copy()

                if not base[i] in lista:
                    lista.append(base[i])
                    if len(lista) == rSize:
                        if not lista in result:
                            result.append(lista)
            if times == 0 and points:
                points.remove(points[0])
            else:
                if len(points) > times:
                    points.remove(points[times])

        return result

    def ehVazio(self):
        if len(self.conjunto) == 0:
            return True
        
        return False
        

    def contidoPropriamente(self, elemento):
        if len(elemento.conjunto) < len(self.conjunto):
            for i in elemento.conjunto:
                if i not in self.conjunto:
                    return False
            return True
        return False
        
    def produto_cartesiano(self,elemento): 
        coordenadas = Conjunto()        
        for i in self.conjunto:
            for j in elemento.conjunto:
                coordenadas.inserir((i,j))
        return coordenadas
    
    def toString(self):
        result = '{'
        for i in range(len(self.conjunto)):
            if type(self.conjunto[i]) == type(Conjunto()):
                if i < len(self.conjunto)-1:
                    result += self.conjunto[i].toString() + ', '
                else:
                    result += self.conjunto[i].toString()
            else:
                if i < len(self.conjunto)-1:
                    result += (str(self.conjunto[i]) + ', ')
                else:
                    result += str(self.conjunto[i])
        return result + '}'