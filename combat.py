import pyautogui  # Biblioteca para simular cliques e interações com a tela
import time  # Biblioteca para criar pausas entre as ações
import random  # Biblioteca para gerar valores aleatórios
# Importa configurações de combate e intervalo de ação
from config import COORDENADAS_BOTAO_COMBATE, ATRASO_ACAO

# Função para iniciar uma batalha no jogo


def iniciar_batalha():
    # Clica nas coordenadas do botão de combate
    pyautogui.click(COORDENADAS_BOTAO_COMBATE)
    # Aguarda um intervalo aleatório para simular comportamento humano
    time.sleep(random.uniform(*ATRASO_ACAO))

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
