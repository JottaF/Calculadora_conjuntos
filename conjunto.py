class Conjunto:
    def __init__(self):
        self.conjunto = []
        self.nome = 'Sem nome'
    
    def nomear(self, nome):
        self.nome = nome
    
    def inserir(self, elemento):
              self.conjunto.append(str(elemento))
    
    def imprimir(self):
        print(self.nome,'= {', (', ').join(sorted(self.conjunto)), '}')

    def tamanho(self):
        print(len(self.conjunto))
        
    def pertence(self, elemento):
        return elemento in self.conjunto

    def contido(self, elemento):
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
    
    # def __addCDP__(self, size, conjunto):

        # print('entrou na função\n')
        # if len(conjunto) and size <= len(conjunto):
        #     print('entrou no if\n')
        #     result = Conjunto()
        #     size = size
        #     index = 0

        #     print('size: ', size,'\nindex: ',index)

        #     a = []

        #     for i in range(len(conjunto)):
        #         print('posição: ',conjunto[i])
        #         if size == 0:
        #             result.inserir(i)
        #             a.append(i)
        #         else:
        #             print('entrou no else\n')
        #             sub = Conjunto()
        #             b = []
        #             if (index + size) <= len(conjunto):
        #                 for j in range(size):
        #                     print(index,size, len(conjunto))
        #                     sub.inserir(conjunto[index+j])
        #                     b.append(index+j)
                    
        #             sub.imprimir()
        #             result.inserir(sub)
        #             a.append(b)
        #             print(a)
        #         index += 1

        #     return result.inserir(self.__addCDP__(size+1, conjunto))

    
    def conjuntoDasPartes(self):
        conjunto = []
        conjunto.append([])

        for i in self.conjunto:
            conjunto.append([i])
        
        

        return conjunto

