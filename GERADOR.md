# Gerador de Senhas Criptograficamente Seguro 🛡️

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Security](https://img.shields.io/badge/Security-000000?style=for-the-badge&logo=hackthebox&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

Este projeto foi desenvolvido como parte dos meus estudos em **Análise e Desenvolvimento de Sistemas (ADS)**, focando nas disciplinas de **Redes e Segurança** e **Software Básico**. Trata-se de uma ferramenta robusta para geração de credenciais seguras via terminal.

## 🧠 Conceitos Aplicados

Neste desenvolvimento, apliquei conceitos fundamentais de segurança digital:

* **Entropia de Dados:** Uso do módulo `secrets` em vez do `random` para garantir aleatoriedade de nível criptográfico (imprescindível em Redes e Segurança).
* **Modularização:** Código estruturado em funções reutilizáveis, facilitando a manutenção e a integração em outros sistemas.
* **Validação de Input:** Tratamento rigoroso de erros para evitar falhas durante o tempo de execução (Software Básico).

## 🚀 Funcionalidades

- [x] Definição de comprimento entre 6 e 16 caracteres.
- [x] Seleção personalizada de caracteres (Maiúsculas, Minúsculas, Números e Símbolos).
- [x] Proteção contra geração de senhas vazias.
- [x] Interface interativa via linha de comando.

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
    print(f"Senha gerada: {senha}")
