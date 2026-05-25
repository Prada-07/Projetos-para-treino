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
                    servico, senha = [p.strip() for p in linha
