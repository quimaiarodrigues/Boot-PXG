import tkinter as tk  # Biblioteca para criar interfaces gráficas.
import threading  # Biblioteca para criar threads (execuções paralelas).
import time  # Biblioteca para criar pausas entre ações.
from movement import toggle_recording, play_recorded_route, record_route, is_route_recorded, move_around
from vision import find_pokemon  # Função para localizar um Pokémon na tela.
# Funções para iniciar e controlar um combate.
from combat import start_battle, use_skill
# Biblioteca para manipular e focar janelas do sistema.
import pygetwindow as gw

# Variável para controlar o estado do bot (ligado/desligado).
bot_running = False

# Função para focar na janela do jogo automaticamente.


def focus_game_window():
    """
    Foca na janela do jogo automaticamente, se encontrada.
    Traz a janela do jogo para frente para que o bot possa interagir com ela.
    """
    try:
        window = gw.getWindowsWithTitle('PoKeXGames')[0]
        window.activate()  # Traz a janela para frente e a foca.
        print("Janela do jogo focada.")
    except IndexError:
        print("Janela do jogo não encontrada. Certifique-se de que o jogo está aberto.")

# Função que retorna o estado do bot.


def is_bot_running():
    global bot_running
    return bot_running

# Função que controla o bot.


def run_bot():
    global bot_running
    print("Iniciando o bot...")
    focus_game_window()

    while bot_running:
        pokemon_position = find_pokemon(
            "C:/Users/ICARO/Desktop/PXG/resized_pokemon_templates/")
        play_recorded_route(is_bot_running)
        time.sleep(1)

    print("Bot parou de executar.")

# Função chamada pelo botão para ligar/desligar o bot.


def toggle_bot():
    global bot_running
    if bot_running:
        bot_running = False
        toggle_button.config(text="Ligar")
        print("Bot desligado.")
    else:
        bot_running = True
        toggle_button.config(text="Desligar")
        print("Bot ligado.")
        threading.Thread(target=run_bot).start()


# Criação da janela principal da interface.
window = tk.Tk()
window.title("Controle do Bot PXG")

# Cria um botão para ligar/desligar o bot.
toggle_button = tk.Button(window, text="Ligar", command=toggle_bot, width=15)
toggle_button.pack(pady=10)

# Cria um botão para gravar a rota.
record_button = tk.Button(window, text="Gravar Rota",
                          command=lambda: toggle_recording(record_button), width=15)
record_button.pack(pady=10)

# Define o tamanho da janela.
window.geometry("300x200")

# Vincula as teclas de seta para gravar a rota.
window.bind('<Up>', lambda event: record_route('up'))
window.bind('<Down>', lambda event: record_route('down'))
window.bind('<Left>', lambda event: record_route('left'))
window.bind('<Right>', lambda event: record_route('right'))

# Inicia o loop da interface gráfica.
window.mainloop()
