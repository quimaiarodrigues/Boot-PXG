import pyautogui
import random
import time
from config import BATTLE_BUTTON_COORDS, ACTION_DELAY

# Função para iniciar uma batalha.


def start_battle():
    pyautogui.click(BATTLE_BUTTON_COORDS)
    time.sleep(random.uniform(*ACTION_DELAY))

# Função para usar uma habilidade durante a batalha.


def use_skill(skill_button_coords):
    pyautogui.click(skill_button_coords)
    time.sleep(random.uniform(*ACTION_DELAY))

# Função para fugir de uma batalha.


def flee_battle():
    pyautogui.click(BATTLE_BUTTON_COORDS)
    time.sleep(random.uniform(*ACTION_DELAY))
