#Fazer um sisteminha de listas
#Precisa inserir, remover e listar
#Sugestao de lista de compras
import time
import os
#lista_compras = []
lista_itens = []
sair = False
opcao= 0
print('SEJA BEM VINDO A LISTA DE COMPRAS')

while sair != True:
    
    print('Informe o Número da opção: ')
    print('1 Inserir comida na lista')
    print('2 Remover comida da lista')
    print('3 Mostrar Lista')
    print('4 SAIR')
    opcao = input('')
    
    try:
        opcao = int(opcao)
    except ValueError:
        print('Você não digitou um número válido!')
        continue
        
 
    if opcao > 4 or opcao < 0:
        print('Número incorreto, tente novamente!')
        continue
    match opcao:
        case 1:
            os.system('clear')
            nome = ''
            nome = input('Informe o nome do item: ').upper()
            lista_itens.append(nome)
            for i in range(4):
                time.sleep(0.5)
                print('.', end='', flush=True)
            print(f'O item: {nome} adicionado à lista!')
            time.sleep(2)
            os.system('clear')
            continue
        case 2:
            os.system('clear')
            item_nome = ''
            print('Para remover o item escreva o nome dele:\n')
            item_nome = input('-->: ')
            if item_nome.upper() in lista_itens:
              for indice, item in enumerate(lista_itens):
                  if item ==   item_nome.upper():
                      lista_itens.pop(indice)
              print('Removido com sucesso!!!')
            else:
                print('Nada encontrado!!!')
                continue
        case 3:
            os.system('clear')
            print('A lista atualizada:')
            if len(lista_itens) > 0:
                for indice, item in enumerate(lista_itens):
                    print(f'{indice +1} --> {item}')
            else:
                print('Lista vazia!!!')
               
        case 4: 
            os.system('clear')
            print('Saindo')
            for i in range(4):
                time.sleep(0.5)
                print('.', end='', flush=True)
            
            sair = True
