class Conjunto:
    def __init__(self, *arg, **args):
        self.conjunto = []
        self.nome = 'Sem nome'
    
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
        return len(self.conjunto)
        
    def pertence(self, elemento):
        return elemento in self.conjunto

    def contido(self, elemento):
        for i in self.conjunto:
            if i not in elemento.conjunto:
                return False

        return True
    
    def contidoPropriamente(self, elemento):
        if elemento.conjunto < self.conjunto:
            for i in elemento:
                if i not in self.conjunto:
                    return False
            return True
        return False
    
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
        conjunto = []
        conjunto.append([])

        for i in self.conjunto:
            conjunto.append([i])
        
        

        return conjunto

