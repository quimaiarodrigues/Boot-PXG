import cv2  # Biblioteca para manipulação de imagens e vídeo
import pyautogui  # Biblioteca para captura de tela
import numpy as np  # Biblioteca para operações com arrays e manipulação de dados numéricos
import os  # Biblioteca para manipulação de diretórios

# Captura a tela e converte para o formato adequado para o OpenCV


def capturar_tela():
    captura = pyautogui.screenshot()  # Tira um print da tela
    captura = np.array(captura)  # Converte a captura para um array NumPy
    # Converte a captura para BGR, formato do OpenCV
    return cv2.cvtColor(captura, cv2.COLOR_RGB2BGR)

# Encontra um Pokémon na tela usando uma pasta com imagens modelo (templates)


def localizar_pokemon(pasta_templates, limite=0.6, escala=(0.5, 1.5), passo_escala=0.1):
    tela = capturar_tela()  # Captura a tela
    # Converte a tela para escala de cinza
    tela_cinza = cv2.cvtColor(tela, cv2.COLOR_BGR2GRAY)

    # Varre cada arquivo na pasta de templates
    for arquivo in os.listdir(pasta_templates):
        if arquivo.endswith(".png"):
            caminho_template = os.path.join(pasta_templates, arquivo)
            template = cv2.imread(caminho_template, cv2.IMREAD_GRAYSCALE)

            if template is None:
                print(f"Erro ao carregar o template: {caminho_template}")
                continue

            # Tenta encontrar correspondência em diferentes tamanhos do template
            for escala_atual in np.arange(escala[0], escala[1], passo_escala):
                largura_nova = int(template.shape[1] * escala_atual)
                altura_nova = int(template.shape[0] * escala_atual)
                template_redimensionado = cv2.resize(
                    template, (largura_nova, altura_nova))

                # Realiza a correspondência do template na tela
                resultado = cv2.matchTemplate(
                    tela_cinza, template_redimensionado, cv2.TM_CCOEFF_NORMED)
                _, valor_maximo, _, localizacao_maxima = cv2.minMaxLoc(
                    resultado)

                # Se o valor de correspondência for maior que o limite, considera o Pokémon encontrado
                if valor_maximo >= limite:
                    print(f"Pokémon encontrado com o template {caminho_template} na escala {
                          escala_atual} com correspondência: {valor_maximo}")

                    # Desenha um retângulo ao redor do Pokémon encontrado
                    topo_esquerdo = localizacao_maxima
                    inferior_direito = (
                        topo_esquerdo[0] + largura_nova, topo_esquerdo[1] + altura_nova)
                    cv2.rectangle(tela, topo_esquerdo,
                                  inferior_direito, (0, 255, 0), 2)

                    # Exibe a tela com o retângulo ao redor do Pokémon
                    cv2.imshow("Pokémon Encontrado", tela)
                    # Aguarda até que uma tecla seja pressionada
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    # Retorna a posição e o tamanho do Pokémon encontrado
                    return localizacao_maxima, (largura_nova, altura_nova)

    print("Nenhum Pokémon encontrado.")
    return None  # Retorna None se nenhum Pokémon for encontrado
