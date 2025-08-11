#  Crie uma lista preenchida com os 5 primeiros colocados de um Campeonato de Futebol, na ordem de colocação

def main():
    
    i = 0
    lista = []  # cria a lista

    while i != 5:
        
        jogador_escolhido = input("Insira o nome dos jogadores que quiser na lista")
        lista.append(jogador_escolhido)
        i = i + 1

    print(lista)

if __name__ == '__main__':  # para mostrar que esse é o programa principal
    main()