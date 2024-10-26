import string
import random

def menu_principal():
    print('''Bem vindo ao sistema de gerador de senhas
          Selecione a opção desejada:
          1 - Definir tamanho
          2 - Definir número de caracteres especiais
          3 - Definir número de letras maíuscula
          4 - Definir quantidade de números
          5 - Gerar senha
          0 - Sair

          Obs.: Por padrão, o tamanho é 12 caracteres, possui 2 caracteres especiais, entre 4 maíusculas e 2 números''')
    opcao = int(input(''))
    return opcao

def gerar_senha(tamanho, qnt_caract_especiais, qnt_letras_maiuscula, qnt_numeros):
    soma_caracteres = qnt_caract_especiais + qnt_letras_maiuscula + qnt_numeros
    if soma_caracteres > tamanho:
        return f"""Valor inválido! Ajuste o tamanho dos caracteres para não ultrapassar o tamanho da senha
              Valores atuais:
              Tamanho: {tamanho}
              Quantidade de Caracteres especiais: {qnt_caract_especiais}
              Quantidade de letras maiúsculas: {qnt_letras_maiuscula}
              Quantidade de números: {qnt_numeros}"""
    else:
        senha = ''
        caracteres_minusculos = string.ascii_lowercase
        caracteres_maiusculos = string.ascii_uppercase
        caracteres_especiais = string.punctuation
        caracteres_numeros = string.digits
        

        for i in range(qnt_caract_especiais):
            senha += random.choice(caracteres_especiais)

        for i in range(qnt_letras_maiuscula):
            senha += random.choice(caracteres_maiusculos)

        for i in range(qnt_numeros):
            senha += random.choice(caracteres_numeros)

        for i in range(tamanho - qnt_caract_especiais - qnt_letras_maiuscula - qnt_numeros):
            senha += random.choice(caracteres_minusculos)

        senha = list(senha)

        random.shuffle(senha)

        return ''.join(senha)
    

def obter_valores_padroes():
    tamanho = 12
    qnt_caract_especiais = 2
    qnt_letras_maiuscula = 4
    qnt_numeros = 2
    senha = gerar_senha(tamanho, qnt_caract_especiais, qnt_letras_maiuscula, qnt_numeros)
    return senha

def iniciar_sistema():
    
    # Definindo as variáveis
    tamanho = 0
    num_especiais = 0
    num_maiusculas = 0
    num_numeros = 0

    opcao = True
    while opcao:
        opcao_menu = menu_principal()
        match opcao_menu:
            case 1:
                tamanho = int(input('Defina o tamanho da senha: '))
            case 2:
                num_especiais = int(input('Defina o tamanho de caracteres especiais: '))
            case 3:
                num_maiusculas = int(input('Defina a quantidade de letras maiusculas: '))
            case 4:
                num_numeros = int(input('Defina a quantidade de números: '))
            case 5:
                if tamanho > 0: 
                    senha = gerar_senha(tamanho, num_especiais, num_maiusculas, num_numeros)
                    print(senha)
                else:
                    print(obter_valores_padroes())
            case 0:
                opcao = False
                print('Saindo do programa!')

iniciar_sistema()
