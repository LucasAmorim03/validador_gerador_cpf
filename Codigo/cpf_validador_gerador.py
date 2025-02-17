#### Validador e Gerador de CPFs brasileiros ####
import os
import sys
import re
import random

while True:
    # Exibe o menu para escolha
    print(
        """ 
        =========================
        |       MENU CPF        |
        |-----------------------|
        | [V] Validar CPF       |
        | [G] Gerar CPF         |
        | [S] Sair              |
        =========================
    
    """
    ) 
    
    # Captura a escolha do usuário e converte para maiúsculo
    menu = input("Escolha uma opção digitando 'V', 'G' ou 'S' -> ").upper()
    os.system('cls') 

    if menu == 'V':

        entrada = input('Digite o CPF: ')

        # Permite apenas números e os caracteres '.' e '-'
        if not re.match(r'^[0-9.-]+$', entrada): 
            print("Entrada inválida! Digite apenas números ou um formato correto.")
            continue
        
        # Remove caracteres não numéricos do CPF
        cpf_usuario = re.sub(r'[^0-9]', '', entrada)
        nove_digitos = cpf_usuario[:9] # Captura os 9 primeiros dígitos
          
        # Armazena uma sequência repetida do primeiro caractere
        verify_rep = cpf_usuario[0] * len(cpf_usuario)

        #  Verifica se o CPF é uma sequência repetida, o que o tornaria inválido
        if verify_rep == cpf_usuario:
            print('Digite uma sequência válida.')
            continue
        
        ## Cálculo do primeiro dígito verificador ##
        contagem_decrescente_1 = 10  # Reinicializa a contagem
        calculo_vezes_1 = 0
       
        # Percorre o iterável para multiplicar cada um dos 9 números
        for item in nove_digitos:
            calculo_vezes_1 += int(item) * contagem_decrescente_1
            contagem_decrescente_1 -= 1

        # Multiplica o valor e acha o resto, representando a penultima etapa do processo do cpf
        calculo_final_1 = (calculo_vezes_1 * 10) % 11
        
        # Confere se o primeiro dos dois últimos dígitos do cpf é maior que 9
        calculo_final_1 = calculo_final_1 if calculo_final_1 <= 9 else 0

        ## Cálculo do segundo dígito verificador ##

        contagem_decrescente_2 = 11
        dez_digitos = nove_digitos + str(calculo_final_1)
        calculo_vezes_2 = 0
        # Percorre o iterável para multiplicar cada um dos 10 números
        for item in dez_digitos:
            calculo_vezes_2 += int(item) * contagem_decrescente_2
            contagem_decrescente_2 -= 1

        # Multiplica o valor e acha o resto, representando a penultima etapa do processo do cpf
        calculo_final_2 = (calculo_vezes_2 * 10) % 11
        
        # Confere se o ultimo dígito do cpf é maior que 9.
        calculo_final_2 = calculo_final_2 if calculo_final_2 <= 9 else 0

        # Forma o CPF completo para validação
        cpf_validado = f'{nove_digitos}{calculo_final_1}{calculo_final_2}'
        
        # Compara o CPF gerado com o informado pelo usuário
        if cpf_validado == cpf_usuario:
            print(f'Seu CPF de número: {cpf_usuario} -> Válido!')
        else:
            print('Cpf inválido!')
        
    elif menu == 'G':
        # Gera 9 primeiros dígitos aleatórios
        nove_digitos = ''

        # Usa o Módulo random para gerar 9 números
        for i in range(9):
            nove_digitos += str(random.randint(0, 9))

         ## Cálculo do primeiro dígito verificador ##
        contagem_decrescente_1 = 10  # Reinicializa a contagem
        calculo_vezes_1 = 0

        # Percorre o iterável para multiplicar cada um dos 9 números
        for item in nove_digitos:
            calculo_vezes_1 += int(item) * contagem_decrescente_1
            contagem_decrescente_1 -= 1

        # Multiplica o valor e acha o resto, representando a penultima etapa do processo do cpf
        calculo_final_1 = (calculo_vezes_1 * 10) % 11
        
        # Confere se o primeiro dos dois últimos dígitos do cpf é maior que 9
        calculo_final_1 = calculo_final_1 if calculo_final_1 <= 9 else 0

        ## Cálculo do segundo dígito verificador ##

        contagem_decrescente_2 = 11
        dez_digitos = nove_digitos + str(calculo_final_1)
        calculo_vezes_2 = 0
        # Percorre o iterável para multiplicar cada um dos 10 números
        for item in dez_digitos:
            calculo_vezes_2 += int(item) * contagem_decrescente_2
            contagem_decrescente_2 -= 1

        # Multiplica o valor e acha o resto, representando a penultima etapa do processo do cpf
        calculo_final_2 = (calculo_vezes_2 * 10) % 11
        
        # Confere se o ultimo dígito do cpf é maior que 9.
        calculo_final_2 = calculo_final_2 if calculo_final_2 <= 9 else 0

        # Gera o CPF válido com os digitos verificadores 
        cpf_validado = f'{nove_digitos}{calculo_final_1}{calculo_final_2}'
        
        print(f'CPF gerado: {cpf_validado}')

    elif menu == 'S':
        print('Saíndo...')
        sys.exit() #Finaliza o programa;
    else:
        os.system('cls') # Limpa a tela antes de exibir a mensagem de erro 
        print("Entrada inválida.")


