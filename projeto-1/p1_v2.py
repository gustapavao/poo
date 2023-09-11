import random, os, sys

class Lista:

 
    # ----------------------------------------------------------------------
    # Atributos
    __lstValores = None
    __DIRATUAL   = os.path.dirname(os.path.abspath(__file__)) 
    __ORDENACOES = ['Bubble', 'Selection', 'Insertion', 'Quick']

    # ----------------------------------------------------------------------
    # Método Construtor
    def __init__(self, *args):
        if len(args) == 3 and isinstance(args[0], int) and isinstance(args[1], int) and isinstance(args[2], int):
            self.__lstValores = [random.randint(args[1], args[2]) for _ in range(args[0])]
        elif len(args) == 1 and isinstance(args[0], str):
            try:
                arquivo = open(self.__DIRATUAL + '\\' + args[0], 'r')
            except FileNotFoundError:
                self.__lstValores = 'ERRO: Arquivo Não Encontrado...'
            except:
                self.__lstValores = f'ERRO: {sys.exc_info()[0]}...'
            else:
                self.__lstValores = list()
                while True:
                    valor = arquivo.readline()[:-1]
                    if not valor: break
                    self.__lstValores.append(int(valor))
                arquivo.close()
        else:
            self.__lstValores = 'ERRO: Argumentos Inválidos ou Incompletos'

    # ----------------------------------------------------------------------
    @property
    def ListaValores(self):
        return self.__lstValores
        
    # ----------------------------------------------------------------------
    def Ordena(self, lista_valores: list, metodo_ordenacao: str):
        if metodo_ordenacao not in selc.__ORDENACOES: 
            return lista_valores

        ...

    # ----------------------------------------------------------------------
    def __bubble(self, lista_valores: list):
        ...

    # ----------------------------------------------------------------------
    def __insertion(self, lista_valores: list):
        ...

    # ----------------------------------------------------------------------
    def __selection(self, lista_valores: list):
        ...

    # ----------------------------------------------------------------------
    def __quick(self, lista_valores: list):
        ...
