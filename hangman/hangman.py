
"""Jogo da forca

$ py teste.py
--------------------------------------------------
                     Hangman
--------------------------------------------------

                  -> * * * * <-

Tentativas:
Dica: palavra com [ 4 ] letras.           Vidas: 5

Escolha uma letra:

"""

__version__ = "0.1.0"
__author__ = "MykeBueno"
__license__ = "unlicense"

import serial
import os
from random import choice
from time import sleep

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def line(caracter='*', tam=50):
    print(f'{caracter}'*tam)

def title(text='', tam=50):
    print(f"{f'{text.title()}':^{tam}}")
    
def layout_header(text='hangman', tam=50, caracter='*'):
    line(caracter, tam)
    title(text, tam)
    line(caracter, tam)
    
def word(word='', tam=50):
    print()
    print(f"{f'-> {word} <-':^{tam}}")
    print()


#############################################################
palavras = ['girassol', 'casa', 'amor', 'camila', 'gato', 'morgana', 'carro', 'pipoca', 'cinema']
palavra = choice(palavras).upper()

lista_palavra = list(palavra)
new_palavra = list('*'*len(palavra))
lifes = 5

choices = []

while True:
    word_new = ' '.join(new_palavra)
    limpar_terminal()
    layout_header(caracter='-')
    word(word_new)
    print(f"Tentativas: ", f"{''.join(choices)}")
    print(f"{f'Dica: palavra com [{len(palavra):^3}] letras.'} {f'Vidas: {lifes}':>18}")
    if palavra == word_new.replace(' ', ''):
        print()
        print(f"VOCE ACERTOU com {lifes} vidas")
        break
    print()
    if lifes:
        escolha = input('Escolha uma letra: ').upper()


        if escolha in palavra and escolha not in choices:
            # result(resul=True)
            for index, letra in enumerate(palavra):
                if escolha == letra:
                        new_palavra[index] = escolha
        else:
            print('aq')
            # result(resul=False)
            lifes -= 1

    else:
        print(palavra)
        print("Você perdeu!")
        break

    choices.append(escolha)


#############################################################
