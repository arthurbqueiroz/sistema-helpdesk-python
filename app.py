import database

def menu():
    while True:
        print("\n=== Sistema de Gestão de Chamados (Help Desk) ===")
        print("1. Abrir novo chamado")
        print("2. Listar chamados abertos")
        print("3. Fechar um chamado")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            titulo = input("Digite o título do problema: ")
            descricao = input("Descreva o problema detalhadamente: ")
            usuario_id = input("ID do Usuário solicitante (ex: 1 ou 2): ")
            
            # Validação simples para evitar quebra do programa se o ID não for número
            if usuario_id.isdigit():
                database.abrir_chamado(titulo, descricao, int(usuario_id))
            else:
                print("Erro: O ID do usuário deve ser um número.")
                
        elif opcao == '2':
            database.listar_chamados_abertos()
            
        elif opcao == '3':
            chamado_id = input("Digite o ID do chamado que deseja fechar: ")
            if chamado_id.isdigit():
                database.fechar_chamado(int(chamado_id))
            else:
                print("Erro: O ID do chamado deve ser um número.")
                
        elif opcao == '4':
            print("Encerrando o sistema...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()