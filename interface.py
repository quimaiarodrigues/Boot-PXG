import tkinter as tk
import threading
import time
from vision import localizar_pokemon
from combat import marca_alvo
import pygetwindow as gw
from database import salvar_rota, excluir_rota, listar_rotas, carregar_rota
from movement import alternar_gravacao, reproduzir_rota_gravada, existe_rota_gravada, rota_gravada

# Variáveis globais para controle do bot
bot_ativo = False
# Variável para armazenar todas as rotas a serem executadas em sequência
rotas_para_executar = []

# Função para focar na janela do jogo automaticamente


def focar_janela_jogo():
    try:
        janela = gw.getWindowsWithTitle('PoKeXGames')[0]
        janela.activate()
        print("Janela do jogo focada.")
    except IndexError:
        print("Janela do jogo não encontrada. Certifique-se de que o jogo está aberto.")

# Função para ligar/desligar o bot


def alternar_bot():
    global bot_ativo
    if bot_ativo:
        bot_ativo = False
        botao_alternar.config(text="Ligar")
        print("Bot desligado.")
    else:
        bot_ativo = True
        botao_alternar.config(text="Desligar")
        print("Bot ligado.")
        threading.Thread(target=executar_bot).start()

# Função principal do bot


def executar_bot():
    global bot_ativo, rotas_para_executar
    print("Iniciando o bot...")
    focar_janela_jogo()

    while bot_ativo:
        if not rotas_para_executar:
            atualizar_lista_rotas_para_execucao()

        for nome_rota in rotas_para_executar:
            if not bot_ativo:
                break
            movimentos = carregar_rota(nome_rota)
            if movimentos:
                print(f"Executando rota: {nome_rota}")
                reproduzir_rota_gravada(lambda: bot_ativo, movimentos)

                # Procura um Pokémon na tela usando uma imagem de template.
                posicao_pokemon = localizar_pokemon(
                    "C:/Users/ICARO/Desktop/PXG/pokemon_templates_vivo/")
                if posicao_pokemon is not None:
                    marca_alvo(posicao_pokemon)
                else:
                    print("Nenhum Pokémon encontrado após a rota.")

                time.sleep(1)  # Pausa entre execuções de rotas

        print("Ciclo de rotas completo, reiniciando.")

    print("Bot parou de executar.")
# Função para carregar todas as rotas para execução em sequência


def atualizar_lista_rotas_para_execucao():
    global rotas_para_executar
    rotas_para_executar.clear()
    rotas = listar_rotas()
    for nome_rota, _ in rotas:
        rotas_para_executar.append(nome_rota)

# Função para salvar uma nova rota com nome


def salvar_rota_na_interface():
    nome_rota = entrada_nome_rota.get()
    if nome_rota and existe_rota_gravada():
        salvar_rota(nome_rota, rota_gravada)
        atualizar_lista_rotas()
        entrada_nome_rota.delete(0, tk.END)
        print(f"Rota '{nome_rota}' salva com sucesso.")

# Função para excluir uma rota selecionada


def excluir_rota_selecionada():
    nome_rota = lista_rotas.get(tk.ACTIVE)
    if nome_rota:
        excluir_rota(nome_rota)
        atualizar_lista_rotas()
        print(f"Rota '{nome_rota}' excluída com sucesso.")

# Função para atualizar a lista de rotas na interface


def atualizar_lista_rotas():
    lista_rotas.delete(0, tk.END)
    for nome_rota, _ in listar_rotas():
        lista_rotas.insert(tk.END, nome_rota)


# Configuração da interface principal
window = tk.Tk()
window.title("Controle do Bot PXG")

# Botão para ligar/desligar o bot
botao_alternar = tk.Button(
    window, text="Ligar", command=alternar_bot, width=15)
botao_alternar.pack(pady=10)

# Botão para gravar rota
botao_gravar = tk.Button(window, text="Gravar Rota",
                         command=lambda: alternar_gravacao(botao_gravar), width=15)
botao_gravar.pack(pady=10)

# Campo de entrada para nome da rota e botão para salvar
entrada_nome_rota = tk.Entry(window)
entrada_nome_rota.pack(pady=5)
botao_salvar_rota = tk.Button(
    window, text="Salvar Rota", command=salvar_rota_na_interface, width=15)
botao_salvar_rota.pack(pady=5)

# Botão para excluir a rota selecionada
botao_excluir_rota = tk.Button(
    window, text="Excluir Rota", command=excluir_rota_selecionada, width=15)
botao_excluir_rota.pack(pady=5)

# Lista de rotas salvas
lista_rotas = tk.Listbox(window, width=30)
lista_rotas.pack(pady=10)
atualizar_lista_rotas()

# Dimensões da janela
window.geometry("300x450")
window.mainloop()
