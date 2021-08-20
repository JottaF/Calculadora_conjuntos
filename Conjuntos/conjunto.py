class Conjunto:
    def __init__(self, *arg):
        self.conjunto = []
        self.nome = 'nome'

        for i in arg:
            if i not in self.conjunto:
                self.conjunto.append(str(i))
    def nomear(self, nome):
        self.nome = nome
    
    def inserir(self, elemento):
        if elemento not in self.conjunto:
            self.conjunto.append(str(elemento))
        else:
            print('Já possui o elemento ', elemento)
    
    def imprimir(self):
        print(self.nome,'= {', (', ').join(sorted(self.conjunto)), '}')

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
        a = self.conjunto
        lista = [[None]]
        for i in range (len(a)):
            lista.append([a[i]])
            for j in range(1,len(a)):
                if not a[i] == a[j]:
                    if [a[j],a[i]]not in lista:
                        lista.append([a[i],a[j]])
                        
        for i in range(len(a)):
            for e in range(i+1,len(a)):
                for u in range(e+1,len(a)):
                    lista.append([a[i],a[e],a[u]])
                    print('ok')     
        return lista
        
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
        

