# Importa funções de movimento
from movement import mover_personagem, existe_rota_gravada, reproduzir_rota_gravada
from vision import localizar_pokemon  # Função para detectar um Pokémon na tela
from combat import iniciar_batalha, usar_habilidade  # Funções para combate

# Função principal que coordena as ações do bot


def principal():
    print("Iniciando o bot...")

    # Loop que continua até o bot ser interrompido
    while True:
        # Procura por um Pokémon na tela usando templates
        posicao_pokemon = localizar_pokemon(
            "C:/Users/ICARO/Desktop/PXG/resized_pokemon_templates/")

        # Se um Pokémon for encontrado, o bot inicia o combate
        if posicao_pokemon:
            print("Pokémon encontrado, iniciando combate...")
            iniciar_batalha()
            # Exemplo de uso de habilidade em posição fixa
            # usar_habilidade((400, 500))
        else:
            # Caso contrário, o bot continua a explorar aleatoriamente
            print("Nenhum Pokémon encontrado, movendo-se...")
            mover_personagem(existe_rota_gravada)
