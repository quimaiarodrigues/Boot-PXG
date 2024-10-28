# Importações
import cv2
import pyautogui
import numpy as np
import os

# Variável global para armazenar a posição do Pokémon
pokemon_posicao = None

def capturar_tela():
    captura = pyautogui.screenshot()
    captura = np.array(captura)
    return cv2.cvtColor(captura, cv2.COLOR_RGB2BGR)

def localizar_pokemon(pasta_templates, limite=0.75, escala=(0.5, 1.5), passo_escala=0.05):
    global pokemon_posicao
    tela = capturar_tela()
    tela_cinza = cv2.cvtColor(tela, cv2.COLOR_BGR2GRAY)
    tela_cinza = cv2.GaussianBlur(tela_cinza, (5, 5), 0)

    for arquivo in os.listdir(pasta_templates):
        if arquivo.endswith(".png"):
            caminho_template = os.path.join(pasta_templates, arquivo)
            template = cv2.imread(caminho_template, cv2.IMREAD_GRAYSCALE)

            if template is None:
                print(f"Erro ao carregar o template: {caminho_template}")
                continue

            template = cv2.GaussianBlur(template, (5, 5), 0)
            template = cv2.normalize(template, None, 0, 255, cv2.NORM_MINMAX)

            for escala_atual in np.arange(escala[0], escala[1], passo_escala):
                largura_nova = int(template.shape[1] * escala_atual)
                altura_nova = int(template.shape[0] * escala_atual)
                template_redimensionado = cv2.resize(template, (largura_nova, altura_nova))

                resultado = cv2.matchTemplate(tela_cinza, template_redimensionado, cv2.TM_CCOEFF_NORMED)
                _, valor_maximo, _, localizacao_maxima = cv2.minMaxLoc(resultado)

                if valor_maximo >= limite:
                    print(f"Pokémon encontrado com o template {caminho_template} na escala {escala_atual:.2f} com correspondência: {valor_maximo:.2f}")
                    topo_esquerdo = localizacao_maxima
                    inferior_direito = (topo_esquerdo[0] + largura_nova, topo_esquerdo[1] + altura_nova)
                    cv2.rectangle(tela, topo_esquerdo, inferior_direito, (0, 255, 0), 2)

                    cv2.imshow("Pokémon Encontrado", tela)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    pokemon_posicao = localizacao_maxima
                    return pokemon_posicao, (largura_nova, altura_nova)

    print("Nenhum Pokémon encontrado.")
    pokemon_posicao = None
    return None
