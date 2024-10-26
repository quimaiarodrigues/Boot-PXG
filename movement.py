import pyautogui
import time
import random
from config import ACTION_DELAY

recording_route = False
recorded_route = []

# Pressiona uma tecla por um curto período, interrompendo se o bot for desligado.


def press_key(key, duration=0.1, is_bot_running=lambda: True):
    if not is_bot_running():
        return
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

# Alterna o estado de gravação da rota.


def toggle_recording(record_button):
    global recording_route, recorded_route
    if recording_route:
        recording_route = False
        record_button.config(text="Gravar Rota")
        print("Gravação da rota interrompida.")
    else:
        recording_route = True
        recorded_route = []
        record_button.config(text="Gravando...")
        print("Iniciando gravação da rota.")

# Registra a tecla pressionada durante a gravação da rota.


def record_route(key):
    global recording_route, recorded_route
    if recording_route:
        print(f"Tecla {key} gravada.")
        recorded_route.append((key, 0.3))

# Reproduz a rota gravada, se existir.


def play_recorded_route(is_bot_running):
    global recorded_route
    for direction, duration in recorded_route:
        if not is_bot_running():
            break
        press_key(direction, duration=duration, is_bot_running=is_bot_running)
        time.sleep(0.5)

# Verifica se há uma rota gravada.


def is_route_recorded():
    return len(recorded_route) > 0

# Movimenta o personagem usando as teclas de seta de forma aleatória.


def move_around(is_bot_running):
    directions = ['up', 'down', 'left', 'right']
    while is_bot_running():
        direction = random.choice(directions)
        press_key(direction, duration=random.uniform(
            0.2, 0.5), is_bot_running=is_bot_running)
        time.sleep(random.uniform(*ACTION_DELAY))
