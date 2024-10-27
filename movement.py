import pyautogui  # Biblioteca para simular teclas e cliques na tela
import time  # Biblioteca para controlar o tempo de ações
import random  # Biblioteca para gerar valores aleatórios
import keyboard  # Biblioteca para captura de teclas globalmente
import pygetwindow as gw  # Biblioteca para manipulação de janelas do sistema
from config import ATRASO_ACAO  # Importa o atraso entre ações do bot

# Variáveis de gravação
gravando_rota = False  # Flag que indica se a gravação da rota está ativa
rota_gravada = []  # Lista para armazenar movimentos gravados
teclas_pressionadas = set()  # Conjunto que guarda teclas atualmente pressionadas
# Dicionário que armazena o último tempo de gravação para cada tecla
ultimo_tempo_gravado = {}
ultima_tecla_gravada = None  # Variável que armazena o último movimento gravado
intervalo_gravacao = 0.5  # Intervalo mínimo de gravação para evitar duplicação

# Função para pressionar uma tecla ou combinação de teclas


def pressionar_tecla(teclas, bot_ativo=lambda: True):
    if not bot_ativo():
        return

    # Pressiona cada tecla e solta imediatamente para evitar manter pressionado
    if isinstance(teclas, (tuple, list)):
        for tecla in teclas:
            pyautogui.keyDown(tecla)  # Pressiona cada tecla da lista
        for tecla in teclas:
            pyautogui.keyUp(tecla)  # Solta cada tecla
    else:
        pyautogui.keyDown(teclas)  # Pressiona uma tecla simples
        pyautogui.keyUp(teclas)  # Solta a tecla

# Função para focar na janela do jogo automaticamente


def focar_janela_jogo():
    try:
        janela = gw.getWindowsWithTitle('PoKeXGames')[0]
        janela.activate()  # Traz a janela para frente e a foca
        print("Janela do jogo focada.")
    except IndexError:
        print("Janela do jogo não encontrada. Certifique-se de que o jogo está aberto.")

# Alterna o estado de gravação da rota e inicializa/para a escuta de teclas globais


def alternar_gravacao(botao_gravacao):
    global gravando_rota, ultima_tecla_gravada
    if gravando_rota:
        gravando_rota = False
        botao_gravacao.config(text="Gravar Rota")
        print("Gravação da rota interrompida.")
        keyboard.unhook_all()  # Para de escutar teclas globalmente
    else:
        focar_janela_jogo()  # Foca na janela do jogo antes de iniciar a gravação
        gravando_rota = True
        rota_gravada.clear()  # Limpa a rota gravada
        ultimo_tempo_gravado.clear()  # Reseta o tempo de gravação para cada tecla
        ultima_tecla_gravada = None  # Reseta o último movimento gravado
        botao_gravacao.config(text="Gravando...")
        print("Iniciando gravação da rota.")
        iniciar_escuta_teclas()  # Inicia a escuta global das teclas

# Inicia a escuta global de teclas para gravação da rota


def iniciar_escuta_teclas():
    keyboard.on_press_key("up", lambda _: adicionar_tecla("up"))
    keyboard.on_release_key("up", lambda _: remover_tecla("up"))
    keyboard.on_press_key("down", lambda _: adicionar_tecla("down"))
    keyboard.on_release_key("down", lambda _: remover_tecla("down"))
    keyboard.on_press_key("left", lambda _: adicionar_tecla("left"))
    keyboard.on_release_key("left", lambda _: remover_tecla("left"))
    keyboard.on_press_key("right", lambda _: adicionar_tecla("right"))
    keyboard.on_release_key("right", lambda _: remover_tecla("right"))

# Função auxiliar para adicionar tecla pressionada


def adicionar_tecla(tecla):
    teclas_pressionadas.add(tecla)
    gravar_rota()

# Função auxiliar para remover tecla pressionada


def remover_tecla(tecla):
    teclas_pressionadas.discard(tecla)

# Grava a combinação de teclas durante a gravação da rota, evitando duplicações


def gravar_rota():
    global gravando_rota, rota_gravada, teclas_pressionadas, ultimo_tempo_gravado, ultima_tecla_gravada, intervalo_gravacao
    if gravando_rota:
        teclas_atuais = tuple(sorted(teclas_pressionadas))
        tempo_atual = time.time()

        # Grava o movimento se ele for diferente do último ou se o intervalo de gravação passou
        if teclas_atuais and (teclas_atuais != ultima_tecla_gravada or tempo_atual - ultimo_tempo_gravado.get(teclas_atuais, 0) > intervalo_gravacao):
            print(f"Tecla(s) {teclas_atuais} gravada(s).")
            # Grava o movimento sem duração específica
            rota_gravada.append(teclas_atuais)
            ultima_tecla_gravada = teclas_atuais  # Atualiza o último movimento gravado
            # Atualiza o tempo de gravação
            ultimo_tempo_gravado[teclas_atuais] = tempo_atual

# Reproduz uma rota gravada com intervalos entre os movimentos


def reproduzir_rota_gravada(bot_ativo, rota_gravada, intervalo_entre_movimentos=0.35):
    for indice, direcao in enumerate(rota_gravada):
        if not bot_ativo():
            break
        print(f"Executando movimento {
              indice+1}/{len(rota_gravada)}: {direcao}")
        pressionar_tecla(direcao, bot_ativo=bot_ativo)
        time.sleep(intervalo_entre_movimentos)  # Tempo entre movimentos

# Executa todas as rotas salvas em um ciclo contínuo


def executar_rotas_continuamente(bot_ativo, todas_rotas, intervalo_entre_movimentos=0.35):
    while bot_ativo():
        for rota in todas_rotas:
            print("Executando nova rota")
            reproduzir_rota_gravada(
                bot_ativo, rota, intervalo_entre_movimentos)
        print("Ciclo completo de todas as rotas. Reiniciando...")

# Verifica se existe uma rota gravada


def existe_rota_gravada():
    return len(rota_gravada) > 0

# Movimenta o personagem de forma aleatória, comentando diagonais


def mover_personagem(bot_ativo):
    direcoes = [
        'up', 'down', 'left', 'right',
        # ['up', 'right'],    # Diagonal superior direita
        # ['up', 'left'],     # Diagonal superior esquerda
        # ['down', 'right'],  # Diagonal inferior direita
        # ['down', 'left']    # Diagonal inferior esquerda
    ]

    while bot_ativo():
        direcao = random.choice(direcoes)  # Escolhe uma direção aleatória
        pressionar_tecla(direcao, bot_ativo=bot_ativo)
        time.sleep(random.uniform(0.05, 0.1))  # Pausa curta entre movimentos
