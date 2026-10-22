import time
import os
import re

class Aluno:
    nome = ""
    idade = 0
    matricula = 0
    media = 0
    notas1 = 0
    notas2 = 0
    def __init__(self, nome1, idade1, matricula1):
        self.nome = nome1
        self.idade = idade1
        self.matricula = matricula1
    def calcularMedia(self, nota1, nota2):
        self.notas1 = nota1
        self.notas2 = nota2
        if not self.notas1 or not self.notas2:
            return print("Sem notas suficientes")
        else:
            self.media = (float(self.notas1) + float(self.notas2)) / 2
            os.system("cls")
            print(f"A média de {self.nome} é: {self.media:.2f}\n\n")
            input('Digite qualquer tecla para voltar ao Menu')
            os.system("cls")
            print('Voltando ao Menu')
            for i in range(4):
                print('.', end='', flush=True)
            os.system("cls")

    
class SistemaEscolar:
    def __init__(self):
        self.listaAlunos = []
    def cadastrarAluno(self, alunoObjt):
        self.listaAlunos.append(alunoObjt)



opcao = 0
sistema = SistemaEscolar()
while opcao != 4:
    print("########################")
    print("1 - Cadastrar Aluno ####")
    print("2 - Listar Alunos   ####")
    print("3 - Calcular Média  ####")
    print("4 - Sair            ####")
    print("########################")
    opcao = input("Digite sua escolha:")


    if opcao.isdigit(): #funcao ve se a str é numero digito
        opcao = int(opcao) #passo str para int
        os.system("cls")
        if opcao > 4:
            os.system("cls")
            print("Por Favor digite um número")
            print("Voltando a tela Inicial: ")
            for i in range(4):
                time.sleep(1)
                print(".", end="", flush=True)
    
        os.system("cls")#limpa a tela do terminal
    elif not opcao.isdigit():
        os.system("cls")
        print("Opção Inválida.\nDigite um número do Menu\nVoltando ao Menu")            
        for i in range(4):
            time.sleep(1)
            print(".", end="", flush=True)
        os.system("cls")

    match opcao:
        case 1:
            print("Bem vindo ao Cadastramento de ALUNOS:")
            nome = input("Digite o Nome do Aluno: ")
            idade = input("Digite a idade: ")
            matricula = input("Digite a Matrícula: ")
            aux = ""

            os.system("cls")            
            print(f"Nome: {nome}\nIdade: {idade}\nMatrícula: {matricula}\nConfirma?")
            aux = input("\n\nSim ou Não?")
            if re.fullmatch(r"sim|não|s|n|nao", aux, re.IGNORECASE):
                if re.fullmatch(r"sim|s", aux, re.IGNORECASE):
                    os.system("cls")
                    print(f'Adicionando {nome} a lista')
                    aluno1 = Aluno(nome, idade, matricula)
                    sistema.cadastrarAluno(aluno1)
                    for i in range(4):
                        time.sleep(1)
                        print('.', end="", flush=True)
                    os.system("cls")
                    
                elif re.fullmatch(r"n|nao|não", aux, re.IGNORECASE):
                    os.system("cls")
                    print("Voltando ao Menu")
                    for i in range(4):
                        time.sleep(1)
                        print(".", end="", flush=True)
                    os.system("cls")
                else:
                    print("Opção Inválida! ")
                    print("Voltando ao Menu")
                    for i in range(4):
                        time.sleep(1)
                        print(".", end="", flush=True)
                    os.system("cls")
                
        case 2: 
            print('Só um momento enquanto eu faço as buscas: ')
            for i in range(4):
                time.sleep(1)
                print('.', end='', flush=True)
            os.system("cls")
            if sistema.listaAlunos:
                print('Aqui está a lista: ')
                for i in range(len(sistema.listaAlunos)):
                    print(f'{i+1}:')
                    print(f'Nome: {sistema.listaAlunos[i].nome}\nIdade: {sistema.listaAlunos[i].idade}\nMatrícula: {sistema.listaAlunos[i].matricula}')
                    print('\n')
                    time.sleep(0.65)
                print("Para voltar ao menu basta digitar qualquer tecla")
                input("")
                os.system("cls")
            else:
                print('Lista Vazia')
                print('Voltando ao Menu')
                for i in range(5):
                    time.sleep(1)
                    print('.', end="", flush=True)
                os.system("cls")
            
        case 3:
            print("Bem-Vindo às médias ")
            aux1 = input("Digite a matrícula do aluno: ")
            if aux1.isdigit():
                encontrado = False

                for aluno in sistema.listaAlunos:
                    if aluno.matricula == aux1:
                        encontrado = True
                        os.system("cls")
                        print(f'Aluno encontrado!\nNome: {aluno.nome}\nIdade: {aluno.idade}') 
                        print('Digite os valores das notas: ')
                        aux2 = input('Digite a primeira nota: ')
                        aux3 = input('Digite a segunda nota: ')
                        aux1 = input('Confirma? ')
                        if re.fullmatch(r'sim|s', aux1, re.IGNORECASE):
                            aluno.calcularMedia(aux2,aux3)
                        elif re.fullmatch(r'nao|não|n'):
                            os.system("cls")
                            print('Voltando ao menu')
                            for i in range(4):
                                time.sleep(0.5)
                                print('.', end='', flush=True)
                        else:
                            print('Tente novamente\nVoltando ao menu')
                            for i in range(4):
                                time.sleep(0.5)
                                print('.', end='', flush=True)
                            os.system("cls")
                if not encontrado:
                    print("Não achei nada\nVoltando ao Menu")
                    for i in range(4):
                        time.sleep(0.5)
                        print('.', end='', flush=True)
                    os.system("cls")
                    
            else:
                print('Favor digitar uma matrícula\nVoltando')
                for i in range(4):
                    time.sleep(0.5)
                    print('.', end="", flush=True)
        case 4:
            print('Saindo')
            for i in range(4):
                time.sleep(0.5)
                print('.', end="", flush=True)
            os.system("cls")
            opcao = 4

    