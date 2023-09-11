import os
import time
from random import randint

class Sorting:
    def __init__(self, data):
        self.lstValores = data

    @classmethod
    def from_file(cls, nome_arquivo):
        dir_atual = os.path.dirname(os.path.abspath(__file__))
        arquivo_input = os.path.join(dir_atual, nome_arquivo)
        lst_valores = []
        
        with open(arquivo_input, 'r') as arquivo:
            for linha in arquivo:
                valor = int(linha.strip())
                lst_valores.append(valor)
        
        return cls(lst_valores)

    @classmethod
    def random_values(cls, n):
        if n < 0:
            return cls([])
        return cls([randint(1, 1000000) for _ in range(n)])

    def bubble_sort(self):
        print('\nIniciando a Ordenação (Bubble Sort)...\n')
        t_inicial = time.time()
        int_size = len(self.lstValores)
        
        for i in range(int_size):
            for j in range(int_size - i - 1):
                if self.lstValores[j] > self.lstValores[j + 1]:
                    self.lstValores[j], self.lstValores[j + 1] = self.lstValores[j + 1], self.lstValores[j]
        
        t_final = time.time()
        d_time = t_final - t_inicial
        print(f'\nTempo de Execução: {d_time} segundos\n')

    def insertion_sort(self):
        print('\nIniciando a Ordenação (Insertion Sort)...\n')
        t_inicial = time.time()
        
        for i in range(1, len(self.lstValores)):
            key = self.lstValores[i]
            j = i - 1
            while j >= 0 and self.lstValores[j] > key:
                self.lstValores[j + 1] = self.lstValores[j]
                j -= 1
            self.lstValores[j + 1] = key
        
        t_final = time.time()
        d_time = t_final - t_inicial
        print(f'\nTempo de Execução: {d_time} segundos\n')

    def selection_sort(self):
        print('\nIniciando a Ordenação (Selection Sort)...\n')
        t_inicial = time.time()
        
        for i in range(len(self.lstValores)):
            min_idx = i
            for j in range(i + 1, len(self.lstValores)):
                if self.lstValores[j] < self.lstValores[min_idx]:
                    min_idx = j
            self.lstValores[i], self.lstValores[min_idx] = self.lstValores[min_idx], self.lstValores[i]
        
        t_final = time.time()
        d_time = t_final - t_inicial
        print(f'\nTempo de Execução: {d_time} segundos\n')

    def partition(self, low, high):
        pivot = self.lstValores[high]
        i = low - 1
        for j in range(low, high):
            if self.lstValores[j] <= pivot:
                i += 1
                self.lstValores[i], self.lstValores[j] = self.lstValores[j], self.lstValores[i]
        self.lstValores[i + 1], self.lstValores[high] = self.lstValores[high], self.lstValores[i + 1]
        return i + 1

    def quick_sort(self, low=None, high=None):
        if low is None:
            low = 0
        if high is None:
            high = len(self.lstValores) - 1
        if low < high:
            p = self.partition(low, high)
            self.quick_sort(low, p - 1)
            self.quick_sort(p + 1, high)

    def save_to_file(self, nome_arquivo):
        arquivo_output = os.path.join(os.path.dirname(os.path.abspath(__file__)), nome_arquivo)
        with open(arquivo_output, 'w') as arquivo:
            for i in self.lstValores:
                arquivo.write(f'{i}\n')

# Usage example
numeros = Sorting.from_file('valores_nao_ordenados.txt')
# Or use Sorting.random_values(n) to generate random data
numeros.quick_sort()
numeros.save_to_file('valores_ordenados.txt')
