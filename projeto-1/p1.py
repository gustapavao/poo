import time, os
from random import randint
class sorting:
    def __init__(self, *args):
        self.DIRATUAL      = os.path.dirname(os.path.abspath(__file__))
        if len(args) == 3 and isinstance(args[0], int) and isinstance(args[1], int) and isinstance(args[0], int):
            self.lstValores = [randint(args[1], args[2]) for _ in range(args[0])]
        elif len(args) == 1 and isinstance (args[0], str): 
            self.ARQUIVO_INPUT = self.DIRATUAL + f'/{args[0]}'
            try:
                self.arquivo       = open(self.ARQUIVO_INPUT, 'r')
            except FileNotFoundError:
                print('Arquivo não encontrado')
            except:
                print('Erro')
            else:
                self.lstValores    = list()
                while True:
                    valor = self.arquivo.readline()[:-1]
                    if not valor: break
                    self.lstValores.append(int(valor))
                self.arquivo.close()
        else:
            print('None')
    
    def ordena_bubble(self):
        try:
            print('\nIniciando a Ordenação...\n')
            tInicial = time.time()
            intSize = len(self.lstValores)
            for i in range(intSize):
                for j in range(intSize - i - 1):
                    if self.lstValores[j] > self.lstValores[j + 1]:
                        self.lstValores[j], self.lstValores[j + 1] = self.lstValores[j + 1], self.lstValores[j]
            tFinal = time.time()
            dTime  = tFinal - tInicial
            print(f'\nTempo de Execução: {dTime} segundos\n')
        except AttributeError:
            print('Houve um problema!')
    def ordena_insertion(self):
        print('\nIniciando a Ordenação...\n')
        tInicial = time.time()
        for i in range(1, len(self.lstValores)):
            key = self.lstValores[i]
            j = i - 1
            while j >= 0 and self.lstValores[j] > key:
                self.lstValores[j + 1] = self.lstValores[j]
                j -= 1
            self.lstValores[j + 1] = key
        tFinal = time.time()
        dTime  = tFinal - tInicial
        print(f'\nTempo de Execução: {dTime} segundos\n')
    def ordena_selection(self):
        print('\nIniciando a Ordenação...\n')
        tInicial = time.time()
        for i in range(len(self.lstValores)):
            min_idx = i
            for j in range(i + 1, len(self.lstValores)):
                if self.lstValores[j] < self.lstValores[min_idx]:
                    min_idx = j
            self.lstValores[i], self.lstValores[min_idx] = self.lstValores[min_idx], self.lstValores[i]
        tFinal = time.time()
        dTime  = tFinal - tInicial
        print(f'\nTempo de Execução: {dTime} segundos\n')
    def partition(self, values, low, high):
        pivot = values[high]
        i = low -1
        for j in range(low, high):
            if values[j] <= pivot:
             i += 1
             values[j], values[i] =values[i], values[j]
        (values[i+1], values[high]) = (values[high], values[i+1])
        return i+1
    def ordena_quick(self, values=None, low=0, high=None):
        if high is None:
            high = len(self.lstValores)-1
        if low < high:
            p = self.partition(self.lstValores, low, high)
            self.ordena_quick(self.lstValores,low, p - 1)
            self.ordena_quick(self.lstValores, p + 1, high)        
    def salvar_arquivo(self):
        ARQUIVO_OUTPUT = self.DIRATUAL + '/valores_ordenados.txt'
        arquivo = open(ARQUIVO_OUTPUT, 'w')
        try:    
            for i in self.lstValores: arquivo.write(f'{i}\n')
            arquivo.close()
        except:
            print('Houve um erro e não foi possível salvar')

numeros = sorting('pipipipo.txt')
numeros.ordena_bubble()
numeros.salvar_arquivo()