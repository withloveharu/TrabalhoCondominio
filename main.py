from classes import *
lista_aptos = ListaDeAptos()
fila_espera = FilaEspera()

menu_texto = """
----------------------------------------
Sistema de Gestão de Condomínios
----------------------------------------
0 - Sair
1 - Adicionar Torre
2 - Adicionar Apartamento
3 - Listar Apartamentos com Vaga de Garagem
4 - Mostrar Fila de Espera
5 - Remover Apartamento
"""

def adicionar_torre():
    if len(lista_aptos) == 0:
        print("Não é possível adicionar Torres sem apartamentos cadastrados.")
        input("Pressione Enter para continuar.")
    else:
        nome_torre = input("Nome da Torre: ")
        endereco_torre = input("Endereço da Torre: ")
        nova_torre = Torre(nome_torre, endereco_torre)
        if len(lista_aptos) < 10:
            print(str(lista_aptos))
            indice_ap = int(input("Digite o índice do apartamento para esta Torre: "))
            apto = lista_aptos[indice_ap]
            apto.associar_torre(nova_torre)
        else:
            print(str(fila_espera))
            indice_ap = int(input("Digite o número do apartamento na Fila de Espera: "))
            apto = fila_espera[indice_ap]
            apto.associar_torre(nova_torre)

def adicionar_apartamento():
    numero_ap = int(input("Número do Apartamento: "))
    novo_ap = Apartamento(numero_ap)
    if len(lista_aptos) < 10:
        nova_vaga = len(lista_aptos) + 1
        novo_ap.vaga_garagem = nova_vaga
        lista_aptos.inserir_no_fim(novo_ap)
        print("Apartamento adicionado com sucesso.")
    else:
        fila_espera.inserir_na_fila(novo_ap)

def menu():
    while True:
        print(menu_texto)
        opcao = int(input("Opção: "))
        if opcao == 0:
            print("Saindo...")
            break
        elif opcao == 1:
            adicionar_torre()
        elif opcao == 2:
            adicionar_apartamento()
        elif opcao == 3:
            print(str(lista_aptos))
            input("Pressione Enter para continuar.")
        elif opcao == 4:
            print(str(fila_espera))
            input("Pressione Enter para continuar.")
        elif opcao == 5:
            escolha = int(input("Digite 1 para remover da Fila de Espera ou 2 para remover da Lista de Apartamentos: "))
            if escolha == 1:
                print("Removendo o primeiro da Fila de Espera")
                print(str(fila_espera))
                fila_espera.remover_da_fila()
            elif escolha == 2:
                print(str(lista_aptos))
                indice_ap = int(input("Digite o índice do apartamento para remover: "))
                del lista_aptos[indice_ap]
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    menu()