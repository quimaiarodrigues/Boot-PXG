import pyautogui
import time
import random
from config import COORDENADAS_BOTAO_COMBATE, ATRASO_ACAO
from vision import pokemon_posicao

# Função para iniciar uma batalha no jogo


def marca_alvo(posicao_pokemon):
    # Verifica se a posição do Pokémon foi definida
    if posicao_pokemon:
        x, y = posicao_pokemon  # Usa `posicao_pokemon` diretamente
        pyautogui.click(x, y, button='right')
        print(f"Pokémon marcado na posição ({x}, {y})")
    else:
        print("Posição do Pokémon não definida ou não encontrada.")


# Função para usar uma habilidade durante a batalha
def usar_habilidade(coordenadas_habilidade):
    # Clica nas coordenadas da habilidade escolhida
    pyautogui.click(coordenadas_habilidade)
    # Aguarda um intervalo aleatório para simular comportamento humano
    time.sleep(random.uniform(*ATRASO_ACAO))


# Função para fugir de uma batalha
def fugir_batalha():
    # Clica no botão para sair do combate
    pyautogui.click(COORDENADAS_BOTAO_COMBATE)
    # Aguarda um intervalo aleatório para simular comportamento humano
    time.sleep(random.uniform(*ATRASO_ACAO))
