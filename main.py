# Importa funções de outros arquivos para controlar o movimento, visão e combate.
from vision import localizar_pokemon


# Função principal que coordena as ações do bot.


def main():
    # Mensagem indicando que o bot começou a rodar.
    print("Iniciando o bot...")

    # Loop principal.
    while True:
        
        # Procura um Pokémon na tela usando uma imagem de template.
        posicao_pokemon = localizar_pokemon(
            "C:/Users/ICARO/Desktop/PXG/pokemon_templates_vivo/")
        # Se um Pokémon for encontrado, inicia um combate.
        if posicao_pokemon:
            print("Pokémon encontrado, iniciando combate...")
        else:
            # Se nenhum Pokémon for encontrado, o bot move o personagem para explorar.
            print("Nenhum Pokémon encontrado, movendo...")
