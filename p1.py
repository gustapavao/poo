class sorting:
    import time, os
    def __init__(self):
        import os
        self.DIRATUAL      = os.path.dirname(os.path.abspath(__file__)) 
        self.ARQUIVO_INPUT = self.DIRATUAL + '/valores_nao_ordenados.txt'
        self.arquivo       = open(self.ARQUIVO_INPUT, 'r')
        self.lstValores    = list()
        while True:
            valor = self.arquivo.readline()[:-1]
            if not valor: break
            self.lstValores.append(int(valor))
        self.arquivo.close()
    def ordena_bubble(self):
        import time
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
    def ordena_insertion(self):
        import time
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
        import time
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
        for i in self.lstValores: arquivo.write(f'{i}\n')
        arquivo.close()

numeros = sorting()
numeros.ordena_quick()
numeros.salvar_arquivo()