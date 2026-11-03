import os
import time
print('Seja Bem-Vindo(a) à calculadora de trocos!')
contagem = 0
trocado = {}
moedas = [50,25,10,5,3,1]
sair = False
while sair != True:
    saldo = input('Digite um número de 1 até 100 centavos:\n')
    try:
        saldo = int(saldo)
        if saldo > 0 and saldo <= 100:
            for centavos in moedas:
                if saldo >= centavos:
                    contagem  = saldo // centavos
                    saldo = saldo % centavos
                    trocado[centavos] = contagem
            for centavos, vezes in trocado.items():
                print(f'{centavos} : {vezes}')

        else:
            print('Digite um valor válido!\n\n')
            input('Pressione qualquer tecla para voltar...\n')
            os.system('cls')
            print('Voltando')
            for i in range(4):
                time.sleep(0.5)
                print('.', end='', flush=True)
            continue


        if saldo == 0:
            aux = input('Deseja Continuar?\n[S]im ou [N]ão?:\n').lower()
            os.system('cls')

            if 's' == aux:
                print('Voltando ao Menu')
                for i in range(4):
                    time.sleep(0.5)
                    print('.', end='', flush=True)
                os.system('cls')

            elif 'n' == aux:
                os.system('cls')
                print('Saindo')
                for i in range(4):
                    time.sleep(0.5)
                    print('.', end='',flush=True)
                sair = True
            else:
                os.system('cls')
                input('Opção inválida!!!\nAperte qualquer tecla para continuar...\n') 
                os.system('cls')    
                continue   
    except ValueError:
        print('Digite um número válido por favor!\n\n')
        time.sleep(2)
        print('Voltando ao Menu')
        for i in range(4):
            print('.', end='', flush=True)
        os.system('cls')
