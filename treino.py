def menu_principal():
    print("Menu Principal:")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def menu_operacoes():
    print("\nMenu de Operações:")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu principal")
    opcao = input("Escolha uma opção: ")
    return opcao

def main():
    while True:
        opcao_principal = menu_principal()
        
        if opcao_principal == '1':
            print("Opção escolhida: Estudantes")
            opcao_operacoes = menu_operacoes()
            if opcao_operacoes == '5':
                continue
            else:
                print("Fim da aplicação.")
                break
        elif opcao_principal == '2':
            print("Opção escolhida: Disciplinas")
            opcao_operacoes = menu_operacoes()
            if opcao_operacoes == '5':
                continue
            else:
                print("Fim da aplicação.")
                break
        elif opcao_principal == '3':
            print("Opção escolhida: Professores")
            opcao_operacoes = menu_operacoes()
            if opcao_operacoes == '5':
                continue
            else:
                print("Fim da aplicação.")
                break
        elif opcao_principal == '4':
            print("Opção escolhida: Turmas")
            opcao_operacoes = menu_operacoes()
            if opcao_operacoes == '5':
                continue
            else:
                print("Fim da aplicação.")
                break
        elif opcao_principal == '5':
            print("Opção escolhida: Matrículas")
            opcao_operacoes = menu_operacoes()
            if opcao_operacoes == '5':
                continue
            else:
                print("Fim da aplicação.")
                break
        elif opcao_principal == '6':
            print("Saindo da aplicação...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
