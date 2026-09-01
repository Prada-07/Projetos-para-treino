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
import string
import secrets


def adicionar():
    servico = input("Digite o serviço:\n-> ").strip().upper()

    def tamanho_senha():
        while True:
            try:
                tamanho = int(input("Quantas caracteres deseja em sua senha? (6-16)\n-> "))
                if 6 <= tamanho <= 16:
                    return tamanho
                print("Por favor, escolha um valor entre 6 e 16 caracteres")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def escolher_caracteres():
        while True:
            caracteres = ""
            maiusculo = input("Deseja incluir letras maiúsculas? (S/N)\n-> ").strip().upper()
            if maiusculo in ["SIM", "S"]:
                caracteres += string.ascii_uppercase
            elif maiusculo not in ["SIM", "S", "NÃO", "NAO", "N"]:
                print("Por favor, digite uma opção válida. (SIM/NÃO)")
                continue

            minusculo = input("Deseja incluir letras minúsculas? (S/N)\n-> ").strip().upper()
            if minusculo in ["SIM", "S"]:
                caracteres += string.ascii_lowercase
            elif minusculo not in ["SIM", "S", "NÃO", "NAO", "N"]:
                print("Por favor, digite uma opção válida. (SIM/NÃO)")
                continue

            numero = input("Deseja incluir números? (S/N)\n-> ").strip().upper()
            if numero in ["SIM", "S"]:
                caracteres += string.digits
            elif numero not in ["SIM", "S", "NÃO", "NAO", "N"]:
                print("Por favor, digite uma opção válida. (SIM/NÃO)")
                continue

            especial = input("Deseja incluir caracteres especiais? (S/N)\n-> ").strip().upper()
            if especial in ["SIM", "S"]:
                caracteres += string.punctuation
            elif especial not in ["SIM", "S", "NÃO", "NAO", "N"]:
                print("Por favor, digite uma opção válida. (SIM/NÃO)")
                continue

            if not caracteres:
                print("Você deve escolher pelo menos um tipo de caractere.")
                continue
            return caracteres

    def gerar_senha(tamanho, caracteres):
        return "".join(secrets.choice(caracteres) for _ in range(tamanho))

    while True:
        aleatorio = input("Deseja utilizar uma senha aleatória?\n-> ").strip().upper()
        if aleatorio in ["SIM", "S"]:
            tamanho_escolhido = tamanho_senha()
            caracteres_escolhidos = escolher_caracteres()
            senha = gerar_senha(tamanho_escolhido, caracteres_escolhidos)
            print(f"Senha gerada: {senha}")
            break
        if aleatorio in ["NÃO", "NAO", "N"]:
            senha = input("Digite a senha:\n-> ").strip()
            break
        print("Opção inválida. Por favor, digite SIM ou NÃO.")

    with open("minhas_senhas.txt", "a") as arquivo:
        arquivo.write(f"{servico} : {senha}\n")
    print("\nSalvando...")
    print("Salvo!")


def visualizar():
    try:
        escolha = input("Deseja localizar todos os serviços?\n-> ").strip().upper()

        if escolha in ("SIM", "S"):
            with open("minhas_senhas.txt", "r") as arquivo:
                for linha in arquivo:
                    if linha.strip():
                        servico, senha = [p.strip() for p in linha.split(":", 1)]
                        print(f"\n📍 Serviço:{servico} -> Senha:{senha}")
        elif escolha in ("NAO", "NÃO", "N"):
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
                        break

            if not encontrado:
                print("\nServiço não encontrado.")
        else:
            print("\nOpção inválida.")
    except FileNotFoundError:
        print("\nArquivo não encontrado.")


def apagar():
    try:
        with open("minhas_senhas.txt", "r") as arquivo:
            for linha in arquivo:
                item = linha.strip().split(":")
                print(f"\n📍 Serviço:{item[0]} -> Senha:{item[1]}")

        servico = input("Digite o serviço para apagar:\n-> ").strip().upper()
        with open("minhas_senhas.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        encontrado = False
        with open("minhas_senhas.txt", "w") as arquivo:
            for linha in linhas:
                if linha.startswith(servico + " :"):
                    encontrado = True
                else:
                    arquivo.write(linha)

        if encontrado:
            print("\nSenha apagada!")
            while True:
                continuacao = input("\nDeseja apagar outra senha?\n-> ").strip().upper()
                if continuacao in ("SIM", "S"):
                    apagar()
                    break
                if continuacao in ("NÃO", "NAO", "N"):
                    break
                print("\nOpção inválida")
        else:
            print("\nServiço não encontrado.")
    except FileNotFoundError:
        print("\nArquivo não encontrado.")


while True:
    print("\n1 - Adicionar senha")
    print("2 - Visualizar senhas")
    print("3 - Apagar senha")
    print("4 - Sair do sistema")

    opcao = input("\n-> ").strip()

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        visualizar()
    elif opcao == "3":
        apagar()
    elif opcao == "4":
        print("\nSaindo do sistema...")
        break
    else:
        print("\nOpção inválida")
```

---

<p align="center">💡 Projeto desenvolvido para fins educacionais.</p>
