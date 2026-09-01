<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Gerador-Projeto-6C63FF?style=for-the-badge&logo=python&logoColor=white" alt="Gerador">
  <img src="https://img.shields.io/badge/GitHub-Projeto-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</p>

<h1 align="center">⚙️ Gerador</h1>

<p align="center">
  Um projeto em Python desenvolvido para gerar combinações e praticar conceitos fundamentais de programação.
</p>

## 📌 Sobre o projeto

O **Gerador** é um projeto desenvolvido em Python para praticar a criação de valores gerados automaticamente, utilizando lógica de programação, entrada de dados e recursos da linguagem.

Este documento apresenta o objetivo, a tecnologia utilizada, as instruções de execução e o código-fonte do projeto. 🐍

## 🎯 Objetivo do sistema

- Gerar resultados automaticamente de acordo com as regras do programa.
- Praticar estruturas de repetição e decisão.
- Trabalhar com entrada e saída de dados.
- Desenvolver lógica de programação utilizando Python.

## ✨ Recursos

- ⚙️ Geração automática de resultados.
- 🔄 Interação com o usuário pelo terminal.
- 🧠 Aplicação de lógica de programação.
- 💻 Execução simples em ambiente Python.

## 🛠️ Tecnologia utilizada

- **Python 3.x**: linguagem usada no desenvolvimento do projeto.

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

3. Execute o arquivo Python correspondente ao projeto:

```bash
python GERADOR.py
```

> Caso o arquivo Python tenha outro nome ou esteja em uma subpasta, ajuste o caminho do comando conforme a organização do projeto.

## 💻 Exemplo de resultado

```text
Resultado gerado pelo programa.
```

## 📁 Estrutura do projeto

```text
Projetos-para-treino/
├── GERADOR.md      # Documentação do projeto
└── GERADOR.py      # Código do gerador
```

## 💻 Código-fonte
```python
  import secrets
import string

# Função para ler o tamanho da senha desejado pelo usuário.
# Garante que o valor esteja entre 6 e 16 caracteres.
def tamanho_senha():
    while True:
        try:
            tamanho = int(input("Quantas caracteres deseja em sua senha? (6-16)\n-> "))
            if 6 <= tamanho <= 16:
                return tamanho
            else:
                print("Por favor, escolha um valor entre 6 e 16 caracteres")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Função para solicitar ao usuário quais tipos de caracteres incluir.
# Retorna uma string com todos os caracteres possíveis para gerar a senha.
def escolher_caracteres():
    while True:
        caracteres = ""

        # Solicita ao usuário se deseja incluir letras maiúsculas, minúsculas, números e caracteres especiais.  
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

# Função para gerar a senha usando o módulo secrets,
# que fornece um gerador de números aleatórios seguro.
def gerar_senha(tamanho, caracteres):
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

if __name__ == "__main__":
    # Solicita ao usuário o tamanho e os tipos de caracteres.
    tamanho_escolhido = tamanho_senha()
    caracteres_escolhidos = escolher_caracteres()

    # Gera e exibe a senha final.
    senha = gerar_senha(tamanho_escolhido, caracteres_escolhidos)
    print(f"Senha gerada: {senha}")

```
  


## 👤 Autor

Desenvolvido por **Leonardo Prada**.

---

<p align="center">💡 Projeto desenvolvido para fins educacionais.</p>
