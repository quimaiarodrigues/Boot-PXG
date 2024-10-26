import cv2
import os

# Caminho da pasta onde estão os templates dos Pokémon.
input_folder = "C:/Users/ICARO/Desktop/PXG/pokemon_templates/"
output_folder = "C:/Users/ICARO/Desktop/PXG/resized_pokemon_templates/"

# Tamanho desejado para os templates (80x80 é um bom ponto de partida).
desired_size = (80, 80)

# Certifica-se de que a pasta de saída existe.
os.makedirs(output_folder, exist_ok=True)

# Percorre cada arquivo na pasta de templates.
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        # Caminho completo do arquivo de entrada.
        input_path = os.path.join(input_folder, filename)
        # Carrega a imagem do Pokémon.
        image = cv2.imread(input_path)
        # Redimensiona a imagem para o tamanho desejado.
        resized_image = cv2.resize(image, desired_size)
        # Caminho completo para salvar a imagem redimensionada.
        output_path = os.path.join(output_folder, filename)
        # Salva a imagem redimensionada.
        cv2.imwrite(output_path, resized_image)
        print(f"Imagem {filename} redimensionada e salva em {output_path}")
