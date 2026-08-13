# Gerenciador de Credenciais Local 🔑

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Security](https://img.shields.io/badge/Security-Data_Protection-informational?style=for-the-badge&logo=keepassxc&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-Flat_File-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Finalizado-brightgreen?style=for-the-badge)

Este projeto é um sistema de gerenciamento de senhas desenvolvido em **Python** para consolidar conhecimentos de **Manipulação de Arquivos (I/O)**, **Tratamento de Exceções** e **Lógica de Programação**. O software permite o CRUD básico (Criar, Ler e Deletar) de credenciais diretamente em um arquivo local.

---

## 🎯 Objetivo

Desenvolver uma ferramenta utilitária que simule um cofre de senhas simples, focado na organização e persistência de dados fora da memória volátil (RAM), utilizando o sistema de arquivos do computador.

## 🚀 Funcionalidades

* **[ADD]** Registro de novos serviços e senhas com armazenamento persistente.
* **[VIEW]** Visualização completa de todos os registros ou busca filtrada por serviço específico.
* **[DELETE]** Remoção seletiva de registros com reescrita otimizada do arquivo.
* **[ERROR HANDLING]** Sistema robusto contra falhas de arquivo inexistente (`FileNotFoundError`).

## 🛠️ Detalhes Técnicos (ADS)

Este projeto aplica conceitos fundamentais abordados nas disciplinas de:

* **Software Básico:** Interação direta com o Sistema de Arquivos através de chamadas de escrita e leitura (`open`, `readlines`, `startswith`).
* **Redes e Segurança:** Introdução à gestão de identidade e acesso (IAM), demonstrando a importância da custódia de credenciais (neste caso, em formato de texto plano para fins educacionais).

```python
import string
import secrets  # módulo criptograficamente seguro para gerar senhas (melhor que 'random')

def adicionar():
    # Nome do serviço (ex: "GMAIL", "NETFLIX") — normalizado em maiúsculas
    # para facilitar buscas exatas depois (em visualizar() e apagar())
    servico = input("Digite o serviço:\n-> ").strip().upper() 
    
    def tamanho_senha():
        # Fica pedindo o tamanho até o usuário digitar um número válido
        # dentro do intervalo permitido (6 a 16 caracteres)
        while True:
            try:
                tamanho = int(input("Quantas caracteres deseja em sua senha? (6-16)\n-> "))
                if 6 <= tamanho <= 16:
                    return tamanho
                else:
                    print("Por favor, escolha um valor entre 6 e 16 carecteres")
            except ValueError:
                # Captura o caso do usuário digitar algo que não é número (ex: "abc")
                print("Entrada inválida. Digite um número inteiro. ")
    
    def escolher_caracteres():
        # Monta a "cesta" de caracteres possíveis para a senha,
        # de acordo com o que o usuário quiser incluir
        while True:
            caractere = ""    
            maiusculo = input("Deseja incluir letras maiúsculas? (S/N)\n-> ").strip().upper()
            if maiusculo in ["SIM", "S"]:
                caractere += string.ascii_uppercase  # A-Z
            elif maiusculo not in ["SIM", "S", "NÃO", "NAO", "N"]:
                print("Por favor, digite uma opção válida. (SIM/NÃO)")
                continue  # opção inválida: reinicia o loop e pergunta tudo de novo
        
            minusculo = input("Deseja incluir letras minúsculas? (S/N)\n-> ").strip().upper()
            if minusculo in ["SIM", "S"]:
                caractere += string.ascii_lowercase  # a-z
            elif minusculo not in ["SIM", "S", "NÃO", "NAO", "N"]:
                print("Por favor, digite uma opção válida. (SIM/NÃO)")
                continue
            
            numero = input("Deseja incluir números? (S/N)\n-> ").strip().upper()
            if numero in ["SIM", "S"]:
                caractere += string.digits  # 0-9
            elif numero not in ["SIM", "S", "NÃO", "NAO", "N"]:
                print("Por favor, digite uma opção válida. (SIM/NÃO)")
                continue
                
            especial = input("Deseja incluir caracteres especiais? (S/N)\n-> ").strip().upper()
            if especial in ["SIM", "S"]:
                caractere += string.punctuation  # !@#$%¨&* etc.
            elif especial not in ["SIM", "S", "NÃO", "NAO", "N"]:
                print("Por favor, digite uma opção válida. (SIM/NÃO)")
                continue
        
            if not caractere:
                # Usuário respondeu "não" para tudo — não dá pra gerar senha sem nenhum tipo de caractere
                print("Você deve escolher pelo menos um tipo de caractere. ")
                continue
            return caractere

    def gerar_senha(tamanho, caractere):
        # secrets.choice() sorteia caracteres de forma segura (evita padrões previsíveis)
        return ''.join(secrets.choice(caractere) for _ in range(tamanho))

    # Pergunta se o usuário quer senha aleatória (gerada) ou uma senha própria
    while True:
        aleatorio = input("Deseja utilizar uma senha aleatória?\n-> ").strip().upper()
        if aleatorio in ["SIM", "S"]:
            tamanho_escolhido = tamanho_senha()
            caracteres_escolhidas = escolher_caracteres()
            senha = gerar_senha(tamanho_escolhido, caracteres_escolhidas)
            print(f"Senha gerada: {senha}")
            break
        elif aleatorio in ["NÃO", "NAO", "N"]:
            senha = input("Digite a senha:\n-> ").strip()
            break
        else:
            print("Opção inválida. Por favor, digite SIM ou NÃO.")
    
    # Salva no arquivo no formato "SERVICO : senha", uma linha por registro
    # "a" = modo append, então não apaga o que já existe, só adiciona no final
    with open("minhas_senhas.txt", "a") as arquivo: 
        arquivo.write(f"{servico} : {senha}\n") 
    print("\nSalvando...")
    print("Salvo!")
    
def visualizar():    
    try:
        escolha = input("Deseja localizar todos os serviços?\n-> ").strip().upper()
        
        if escolha in ("SIM", "S"):
            # Lista todos os serviços salvos, linha por linha
            with open("minhas_senhas.txt", "r") as arquivo:
                for linha in arquivo:
                    if linha.strip():  # ignora linhas em branco
                        # split(":", 1) separa só no primeiro ":", 
                        # evitando problemas se a senha também tiver ":"
                        servico, senha = [p.strip() for p in linha.split(":", 1)]
                        print(f"\n📍 Serviço:{servico} -> Senha:{senha}")
        
        elif escolha in ("NAO", "NÃO", "N"):
            # Busca um serviço específico pelo nome
            localizacao = input("Digite o serviço que deseja localizar:\n-> ").strip().upper()
            encontrado = False
            
            with open("minhas_senhas.txt", "r") as arquivo:
                for linha in arquivo:
                    if not linha.strip():
                        continue
                    servico, senha = [p.strip() for p in linha.split(":", 1)]
                    if servico == localizacao:
                        print(f"\n📍 Serviço:{servico} -> Senha:{senha}")
                        encontrado = True
                        break  # achou, não precisa continuar procurando
            
            if not encontrado:
                print("\nServiço não encontrado.")
        
        else:
            print("\nOpção inválida.")
    
    except FileNotFoundError:
        # Acontece se o usuário tentar visualizar antes de ter adicionado qualquer senha
        print ("\nArquivo não encontrado. ")
        
def apagar():
    try:
        # Mostra todas as senhas salvas antes de perguntar qual apagar
        with open("minhas_senhas.txt", "r") as arquivo:
            for linha in arquivo:
                item = linha.strip().split(":")
                print (f"\n📍 Serviço:{item[0]} -> Senha:{item[1]}")

        servico = input("Digite o serviço para apagar:\n-> ").strip().upper()

        # Lê todas as linhas em memória...
        with open("minhas_senhas.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        encontrado = False
        # ...e reescreve o arquivo do zero ("w" sobrescreve tudo),
        # copiando de volta todas as linhas EXCETO a do serviço escolhido
        with open("minhas_senhas.txt", "w") as arquivo:
            for linha in linhas:
                if linha.startswith(servico + " :"):
                    encontrado = True  # essa é a linha que não será reescrita (ou seja, foi "apagada")
                else:
                    arquivo.write(linha)

        if encontrado:
            print("\nSenha apagada!")
            while True:
                continuacao  = input("\nDeseja apagar outra senha?\n-> ").strip().upper()
                if continuacao in ("SIM", "S"):
                     apagar()  # chama a própria função de novo (recursão) para apagar outra
                elif continuacao in ("NÃO", "NAO", "N"):
                    break
                else: 
                    print ("\nOpção invalida")
        else:
            print("\nServiço não encontrado.")
    except FileNotFoundError:
        print("\nArquivo não encontrado.")
  

# Loop principal do programa: mostra o menu até o usuário escolher sair
while True:        
    print ("\n1- Adicionar Senha. ")
    print ("2- Visualizar Senhar. ")
    print ("3- Apagar Senha. ")
    print ("4- Sair do Sistema. ")

    opcao = input("\n-> ").strip()

    if opcao == "1":
        adicionar()
    elif opcao == "2":
         visualizar()
    elif opcao == "3" :
        apagar()
    elif opcao == "4":
        print ("\nSaindo do Sistema...")
        break
    else:
        print("\nOpção inválida")
