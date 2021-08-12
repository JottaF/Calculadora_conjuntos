class Conjunto:
    def __init__(self, nome):
        self.conjunto = []
        self.nome = nome
    
    def inserir(self, elemento):
              self.conjunto.append(str(elemento))
    
    def imprimir(self):
        print('{', (', ').join(sorted(self.conjunto)), '}')

    def pertence(self, elemento):
        return elemento in self.conjunto

    def contido(self, elemento):
        spot = True
        for i in self.conjunto:
            if i not in elemento.conjunto:
                spot = False
        return spot

    
    def uniao(self, elemento):
        uniao = []
        uniao.copy()
        for i in elemento.conjunto:
            if not i in uniao:
                uniao.append(i)
        
        return sorted(uniao)
