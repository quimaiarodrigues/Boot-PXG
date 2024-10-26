import cv2
import pyautogui
import numpy as np
import os


def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    return cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)


def find_pokemon(template_folder, threshold=0.6, scale_range=(0.5, 1.5), scale_step=0.1):
    screen = capture_screen()
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    # Itera sobre cada imagem de template na pasta
    for filename in os.listdir(template_folder):
        if filename.endswith(".png"):
            template_path = os.path.join(template_folder, filename)
            template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

            if template is None:
                print(f"Erro ao carregar o template: {template_path}")
                continue

            # Varre diferentes tamanhos do template para tentar encontrar uma correspondência
            for scale in np.arange(scale_range[0], scale_range[1], scale_step):
                # Redimensiona o template de acordo com a escala atual
                new_width = int(template.shape[1] * scale)
                new_height = int(template.shape[0] * scale)
                resized_template = cv2.resize(
                    template, (new_width, new_height))

                # Executa a correspondência do template redimensionado na captura de tela
                result = cv2.matchTemplate(
                    screen_gray, resized_template, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, max_loc = cv2.minMaxLoc(result)

                # Verifica se o valor de correspondência é maior que o threshold
                if max_val >= threshold:
                    print(f"Pokémon encontrado com template {template_path} na escala {
                          scale} com correspondência: {max_val}")

                    # Desenha um retângulo ao redor da área correspondente na captura de tela
                    top_left = max_loc
                    bottom_right = (
                        top_left[0] + new_width, top_left[1] + new_height)
                    # Retângulo verde com espessura 2
                    cv2.rectangle(screen, top_left,
                                  bottom_right, (0, 255, 0), 2)

                    # Exibe a captura de tela com o retângulo
                    cv2.imshow("Pokémon Encontrado", screen)
                    # Espera até que uma tecla seja pressionada para fechar a janela
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    # Retorna a posição e o tamanho do Pokémon encontrado
                    return max_loc, (new_width, new_height)

    print("Nenhum Pokémon encontrado.")
    return None
