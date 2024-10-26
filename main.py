# Importa funções de outros arquivos para controlar o movimento, visão e combate.
from movement import move_around
from vision import find_pokemon
from combat import start_battle, use_skill

# Função principal que coordena as ações do bot.


def main():
    # Mensagem indicando que o bot começou a rodar.
    print("Iniciando o bot...")

    # Loop principal.
    while True:
        # Procura um Pokémon na tela usando uma imagem de template.
        pokemon_position = find_pokemon(
            "C:/Users/ICARO/Desktop/PXG/resized_pokemon_templates/")

        # Se um Pokémon for encontrado, inicia um combate.
        if pokemon_position:
            print("Pokémon encontrado, iniciando combate...")
            # start_battle()
            # Usa uma habilidade específica durante o combate.
            # use_skill((400, 500))
        else:
            # Se nenhum Pokémon for encontrado, o bot move o personagem para explorar.
            print("Nenhum Pokémon encontrado, movendo...")
            move_around()
