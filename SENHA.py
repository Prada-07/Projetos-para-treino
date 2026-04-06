
# Criação da função "adicionar", que será responsável pela criação de senhas.
def adicionar():
    servico = input("Digite o serviço: ").upper() 
    senha = input("Digite a senha: ")
    
    # Abertura do arquivo de texto, que irá armazenar os serviços com suas senhas.
    with open("minhas_senhas.txt", "a") as arquivo: 
        # O programa irá escrever no arquivo de texto o serviço e a senha.
        arquivo.write(f"{servico} : {senha}\n") 
        
    print("\nSalvando...")
    print("Salvo!")

# Criação da função "visualizar", responsável por permitir a visualização dos serviços e suas senhas.
def visualizar():    
    try:
        # O programa irá dar a opção ao usúario de escolher localizar apenas uma senha específica, ou todas.
        escolha = input("Deseja localizar todos os serviços? ").strip().upper() 
        
        if escolha in ("SIM", "S"):
            with open("minhas_senhas.txt", "r") as arquivo:
                for linha in arquivo:
                    if linha.strip():
                        # O sistema transforma "serviço" e "senha" em uma lista, os dividindo uma vez. 
                        servico, senha = [p.strip() for p in linha.split(":", 1)] 
                        print(f"\n📍 Serviço:{servico} -> Senha:{senha}") 
        
        elif escolha in ("NAO", "NÃO", "N"):
            # O usuário irá digitar o serviço que deseja localizar.
            localizacao = input("Digite o serviço que deseja localizar: ").strip().upper() 
            # A variável booleana "encontrado" controla se o serviço específico que o usuário digitou foi localizado.
            encontrado = False 
            
            with open("minhas_senhas.txt", "r") as arquivo:
                for linha in arquivo:
                    if not linha.strip():
                        continue
                    servico, senha = [p.strip() for p in linha.split(":", 1)]
                    if servico == localizacao:
                        print(f"\n📍 Serviço:{servico} -> Senha:{senha}")
                        # A variável "encontrado" recebe o valor de verdadeiro, caso o serviço específico seja localizado, e é direcionada para o break.
                        encontrado = True 
                        break
            
            # Como "encontrado" já recebe o valor de falso, ela retorna que nenhum serviço foi localizado, caso o usuário escreva errado o servico, ou ele não exista.
            if not encontrado: 
                print("\nServiço não encontrado.")
        
        else:
            print("\nOpção inválida.")
    
    except FileNotFoundError:
        # Para evitar uma interrupção do programa, se o arquivo não foi encontrado, o programa retorna uma mensagem de "Arquivo não encontrado. ".
        print("\nArquivo não encontrado. ") 

# Criação da função "apagar", responsável pela exclusão de qualquer serviço e senha criados.        
def apagar():
    try:
        # O programa irá exibir todos os serviços e senhas armazenadas, para que o usuário possa escolher qual apagar.
        with open("minhas_senhas.txt", "r") as arquivo:
            for linha in arquivo:
                item = linha.strip().split(":")
                print(f"\n📍 Serviço:{item[0]} -> Senha:{item[1]}") 
        
        servico = input("Digite o serviço para apagar: ").upper()
        
        with open("minhas_senhas.txt", "r") as arquivo:
            # O programa irá ler todas as linhas do arquivo, as retornando como uma lista de strings. 
            linhas = arquivo.readlines() 
            
        encontrado = False
        with open("minhas_senhas.txt", "w") as arquivo:
            for linha in linhas:
                # O programa irá ler os prefixos das strings. Neste caso, o prefixo está sendo classificado como o serviço. 
                if linha.startswith(servico + " :"): 
                    encontrado = True
                else:
                    # O programa irá ler a linha desejada, reencrevendo o arquivo inteiro sem ela.
                    arquivo.write(linha) 
                    
        if encontrado:
            print("\nSenha apagada!")
           
            # O programa irá perguntar se o usuário gostaria de apagar outra senha. Caso o usuário queira, ele executará novamente a função apagar. Ao contrário, seguirá para o break.     
            while True:
                continuacao = input("\nDeseja apagar outra senha? ").upper()
                if continuacao in ("SIM", "S"):
                     apagar() 
                elif continuacao in ("NÃO", "NAO", "N"):
                    break
                else: 
                    print("\nOpção invalida")
        else:
            print("\nServiço não encontrado.")
            
    except FileNotFoundError:
        print("\nArquivo não encontrado.")

# O programa exibirá as opções que o usuário pode escolher e as executará, se a opção estiver dentre as exibidas. 
while True:        
    print("\n1- Adicionar Senha. ")
    print("2- Visualizar Senhar. ")
    print("3- Apagar Senha. ")
    print("4- Sair do Sistema. ")

    opcao = input("\n-> ")

    if opcao == "1":
        adicionar()
    elif opcao == "2":
         visualizar()
    elif opcao == "3":
        apagar()
    elif opcao == "4":
        print("\nSaindo do Sistema...")
        break
    else:
        print("\nOpção inválida")
