<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Segurança-Senhas-2E7D32?style=for-the-badge&logo=letsencrypt&logoColor=white" alt="Segurança">
  <img src="https://img.shields.io/badge/GitHub-Projeto-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</p>

<h1 align="center">🔐 Gerador de Senhas</h1>

<p align="center">
  Um programa em Python criado para gerar senhas aleatórias e personalizadas de forma simples.
</p>

## 📌 Sobre o projeto

O **Gerador de Senhas** é uma aplicação desenvolvida em Python para criar senhas aleatórias a partir de critérios definidos pelo usuário. A proposta é facilitar a criação de combinações mais difíceis de adivinhar para o uso cotidiano.

Este projeto foi desenvolvido para praticar conceitos fundamentais de programação, como entrada de dados, estruturas de repetição, condições, manipulação de textos e geração de valores aleatórios. 🐍

## 🎯 Objetivo do sistema

- Gerar senhas aleatórias de forma rápida.
- Permitir a criação de senhas personalizadas.
- Incentivar o uso de combinações mais fortes.
- Praticar fundamentos da linguagem Python.

## ✨ Recursos

- 🔢 Definição da quantidade de caracteres.
- 🔠 Uso de letras maiúsculas e minúsculas.
- 🔣 Inclusão de números e caracteres especiais.
- 🎲 Geração aleatória de combinações.
- 💻 Execução simples pelo terminal.

## 🛠️ Tecnologia utilizada

- **Python 3.x**: linguagem utilizada no desenvolvimento do programa.

## ▶️ Como executar

### Pré-requisitos

- Ter o [Python](https://www.python.org/downloads/) 3.x instalado.
- Ter acesso a um terminal ou ao Visual Studio Code.

### Execução pelo terminal

1. Clone o repositório:

```bash
git clone https://github.com/Prada-07/Projetos-para-treino.git
```

2. Acesse a pasta do projeto:

```bash
cd Projetos-para-treino
```

3. Execute o arquivo Python correspondente ao gerador de senhas:

```bash
python SENHA.py
```

> Caso o arquivo Python esteja em outra pasta ou possua outro nome, ajuste o caminho do comando conforme a organização do projeto.

## 💻 Exemplo de resultado

```text
Digite o tamanho da senha: 12

Senha gerada: G7@kP2!xQ9#m
```

## 📁 Estrutura do projeto

```text
Projetos-para-treino/
├── SENHA.md       # Documentação do projeto
└── SENHA.py       # Código do gerador de senhas
```

## 🔒 Boas práticas de segurança

- Use senhas diferentes para cada serviço.
- Prefira senhas longas e variadas.
- Evite informações pessoais, como nomes e datas de nascimento.
- Não compartilhe suas senhas com outras pessoas.
- Para contas importantes, considere utilizar um gerenciador de senhas.

> ⚠️ Este projeto tem finalidade educacional. Para sistemas reais, utilize bibliotecas e práticas de segurança adequadas ao contexto da aplicação.

## 👤 Autor

Desenvolvido por **Leonardo Prada**.

## 💻 Código-fonte

```python
# Importa recursos para trabalhar com letras, números e caracteres especiais.
import string

# Importa o módulo secrets, recomendado para gerar valores aleatórios
# com maior segurança.
import secrets


# Função responsável por adicionar uma nova senha.
def adicionar():
    # Solicita o nome do serviço e converte a resposta para letras maiúsculas.
    servico = input("Digite o serviço:\n-> ").strip().upper()

    # Função responsável por solicitar e validar o tamanho da senha.
    def tamanho_senha():
        while True:
            try:
                # Solicita um tamanho inteiro ao usuário.
                tamanho = int(
                    input(
                        "Quantas caracteres deseja em sua senha? (6-16)\n-> "
                    )
                )

                # Verifica se o tamanho está entre 6 e 16 caracteres.
                if 6 <= tamanho <= 16:
                    return tamanho

                # Exibe uma mensagem caso o valor esteja fora do limite.
                print("Por favor, escolha um valor entre 6 e 16 caracteres")

            # Trata entradas que não sejam números inteiros.
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    # Função responsável por escolher os tipos de caracteres da senha.
    def escolher_caracteres():
        while True:
            # Começa com uma lista de caracteres vazia.
            caracteres = ""

            # Pergunta se o usuário deseja utilizar letras maiúsculas.
            maiusculo = input(
                "Deseja incluir letras maiúsculas? (S/N)\n-> "
            ).strip().upper()

            # Adiciona letras maiúsculas à lista de caracteres.
            if maiusculo in ["SIM", "S"]:
                caracteres += string.ascii_uppercase

            # Verifica se a resposta digitada é inválida.
            elif maiusculo not in ["SIM", "S", "NÃO", "NAO", "N"]:
                print("Por favor, digite uma opção válida. (SIM/NÃO)")
                continue

            # Pergunta se o usuário deseja utilizar letras minúsculas.
            minusculo = input(
                "Deseja incluir letras minúsculas? (S/N)\n-> "
            ).strip().upper()

            # Adiciona letras minúsculas à lista de caracteres.
            if minusculo in ["SIM", "S"]:
                caracteres += string.ascii_lowercase

            # Verifica se a resposta digitada é inválida.
            elif minusculo not in ["SIM", "S", "NÃO", "NAO", "N"]:
                print("Por favor, digite uma opção válida. (SIM/NÃO)")
                continue

            # Pergunta se o usuário deseja utilizar números.
            numero = input(
                "Deseja incluir números? (S/N)\n-> "
            ).strip().upper()

            # Adiciona os números de 0 a 9 à lista de caracteres.
            if numero in ["SIM", "S"]:
                caracteres += string.digits

            # Verifica se a resposta digitada é inválida.
            elif numero not in ["SIM", "S", "NÃO", "NAO", "N"]:
                print("Por favor, digite uma opção válida. (SIM/NÃO)")
                continue

            # Pergunta se o usuário deseja utilizar caracteres especiais.
            especial = input(
                "Deseja incluir caracteres especiais? (S/N)\n-> "
            ).strip().upper()

            # Adiciona caracteres especiais à lista de caracteres.
            if especial in ["SIM", "S"]:
                caracteres += string.punctuation

            # Verifica se a resposta digitada é inválida.
            elif especial not in ["SIM", "S", "NÃO", "NAO", "N"]:
                print("Por favor, digite uma opção válida. (SIM/NÃO)")
                continue

            # Impede a criação de uma senha sem caracteres selecionados.
            if not caracteres:
                print("Você deve escolher pelo menos um tipo de caractere.")
                continue

            # Retorna todos os grupos de caracteres escolhidos.
            return caracteres

    # Função responsável por gerar a senha aleatória.
    def gerar_senha(tamanho, caracteres):
        # Escolhe caracteres aleatórios até atingir o tamanho informado.
        return "".join(
            secrets.choice(caracteres)
            for _ in range(tamanho)
        )

    # Pergunta se o usuário deseja gerar uma senha aleatória.
    while True:
        aleatorio = input(
            "Deseja utilizar uma senha aleatória?\n-> "
        ).strip().upper()

        # Caso o usuário confirme, gera uma senha automaticamente.
        if aleatorio in ["SIM", "S"]:
            tamanho_escolhido = tamanho_senha()
            caracteres_escolhidos = escolher_caracteres()

            # Cria a senha utilizando o tamanho e os caracteres escolhidos.
            senha = gerar_senha(
                tamanho_escolhido,
                caracteres_escolhidos
            )

            # Exibe a senha gerada.
            print(f"Senha gerada: {senha}")
            break

        # Caso o usuário não queira uma senha aleatória,
        # permite que ele informe uma senha manualmente.
        if aleatorio in ["NÃO", "NAO", "N"]:
            senha = input("Digite a senha:\n-> ").strip()
            break

        # Exibe uma mensagem caso a opção seja inválida.
        print("Opção inválida. Por favor, digite SIM ou NÃO.")

    # Abre o arquivo no modo de adição para não apagar senhas anteriores.
    with open("minhas_senhas.txt", "a") as arquivo:
        # Salva o serviço e a senha no arquivo.
        arquivo.write(f"{servico} : {senha}\n")

    # Informa ao usuário que a senha está sendo salva.
    print("\nSalvando...")
    print("Salvo!")


# Função responsável por visualizar senhas salvas.
def visualizar():
    try:
        # Pergunta se o usuário deseja visualizar todos os serviços.
        escolha = input(
            "Deseja localizar todos os serviços?\n-> "
        ).strip().upper()

        # Se a resposta for positiva, exibe todas as senhas.
        if escolha in ("SIM", "S"):
            with open("minhas_senhas.txt", "r") as arquivo:
                for linha in arquivo:
                    # Ignora linhas vazias.
                    if linha.strip():
                        # Divide a linha em serviço e senha.
                        servico, senha = [
                            parte.strip()
                            for parte in linha.split(":", 1)
                        ]

                        # Exibe o serviço e sua senha.
                        print(
                            f"\n📍 Serviço:{servico} -> Senha:{senha}"
                        )

        # Se a resposta for negativa, solicita um serviço específico.
        elif escolha in ("NAO", "NÃO", "N"):
            localizacao = input(
                "Digite o serviço que deseja localizar:\n-> "
            ).strip().upper()

            # Controla se o serviço foi encontrado.
            encontrado = False

            with open("minhas_senhas.txt", "r") as arquivo:
                for linha in arquivo:
                    # Ignora linhas vazias.
                    if not linha.strip():
                        continue

                    # Separa o serviço e a senha armazenados.
                    servico, senha = [
                        parte.strip()
                        for parte in linha.split(":", 1)
                    ]

                    # Verifica se o serviço corresponde à busca.
                    if servico == localizacao:
                        print(
                            f"\n📍 Serviço:{servico} -> Senha:{senha}"
                        )
                        encontrado = True
                        break

            # Informa caso nenhum serviço correspondente seja localizado.
            if not encontrado:
                print("\nServiço não encontrado.")

        # Trata respostas diferentes das opções esperadas.
        else:
            print("\nOpção inválida.")

    # Trata a situação em que o arquivo ainda não existe.
    except FileNotFoundError:
        print("\nArquivo não encontrado.")


# Função responsável por apagar uma senha salva.
def apagar():
    try:
        # Abre o arquivo para exibir os serviços disponíveis.
        with open("minhas_senhas.txt", "r") as arquivo:
            for linha in arquivo:
                # Separa o serviço e a senha da linha.
                item = linha.strip().split(":")

                # Exibe o serviço e a senha encontrados.
                print(
                    f"\n📍 Serviço:{item[0]} -> Senha:{item [docs.github](https://docs.github.com/pt)}"
                )

        # Solicita o serviço que será apagado.
        servico = input(
            "Digite o serviço para apagar:\n-> "
        ).strip().upper()

        # Lê todas as linhas do arquivo antes de realizar a alteração.
        with open("minhas_senhas.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        # Controla se alguma senha foi encontrada.
        encontrado = False

        # Abre o arquivo no modo de escrita para regravar seu conteúdo.
        with open("minhas_senhas.txt", "w") as arquivo:
            for linha in linhas:
                # Remove a linha correspondente ao serviço informado.
                if linha.startswith(servico + " :"):
                    encontrado = True
                else:
                    # Mantém todas as outras linhas no arquivo.
                    arquivo.write(linha)

        # Informa que a senha foi apagada.
        if encontrado:
            print("\nSenha apagada!")

            # Pergunta se o usuário deseja apagar outra senha.
            while True:
                continuacao = input(
                    "\nDeseja apagar outra senha?\n-> "
                ).strip().upper()

                # Chama novamente a função para apagar outra senha.
                if continuacao in ("SIM", "S"):
                    apagar()
                    break

                # Encerra a operação caso a resposta seja negativa.
                if continuacao in ("NÃO", "NAO", "N"):
                    break

                # Trata respostas inválidas.
                print("\nOpção inválida")

        # Informa caso o serviço não seja encontrado.
        else:
            print("\nServiço não encontrado.")

    # Trata a situação em que o arquivo ainda não existe.
    except FileNotFoundError:
        print("\nArquivo não encontrado.")


# Mantém o sistema em execução até que o usuário escolha sair.
while True:
    # Exibe o menu principal.
    print("\n1 - Adicionar senha")
    print("2 - Visualizar senhas")
    print("3 - Apagar senha")
    print("4 - Sair do sistema")

    # Solicita a opção desejada.
    opcao = input("\n-> ").strip()

    # Executa a função de adicionar senha.
    if opcao == "1":
        adicionar()

    # Executa a função de visualizar senhas.
    elif opcao == "2":
        visualizar()

    # Executa a função de apagar senha.
    elif opcao == "3":
        apagar()

    # Encerra o programa.
    elif opcao == "4":
        print("\nSaindo do sistema...")
        break

    # Trata opções inexistentes no menu.
    else:
        print("\nOpção inválida")
```


---

<p align="center">💡 Projeto desenvolvido para fins educacionais.</p>
