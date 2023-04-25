'''
================================
Alunos:
LUCAS DOS SANTOS SOARES
RAQUEL SANTOS DA ROCHA
================================
'''
import os

escolha = 0

while escolha != 3:
        os.system('cls')
        print("\n==== SISTEMA DE CADASTRO DA FACOMP ====")
        print("Digite 1 para ENGENHARIA DA COMPUTAÇÃO")
        print("Digite 2 para SISTEMAS DE INFORMAÇÃO")
        print("Digite 3 para SAIR")

        opcao = int(input("\nDigite sua opção: "))

        #ENGENHARIA
        if opcao == 1:
                arquivo_EC = 'Provas/1ª avaliação/alunos_ec.txt'
                escolha_ec = 0

                while escolha_ec != 5:
                        os.system('cls')
                        print("\n==== SISTEMA DE CADASTRO DA FACOMP ====")
                        print("Digite 1 para CADASTRAR")
                        print("Digite 2 para CONSULTAR")
                        print("Digite 3 para ALTERAR")
                        print("Digite 4 para EXCLUIR")
                        print("Digite 5 para RETORNAR")

                        opcao_ec = int(input("\nDigite sua opção: "))

                        #CADASTRAR
                        if opcao_ec == 1:
                                os.system('cls')
                                print("\n==== SISTEMA DE CADASTRO DA FACOMP ====")

                                arquivo = open(arquivo_EC, 'a')

                                arquivo.write(input("Insira a Matrícula: "))
                                arquivo.write("\n")
                                
                                arquivo.write(input("Insira o Nome: "))
                                arquivo.write("\n")

                                print("\nCadastrado com sucesso!")
                                input("\nAperte ENTER para continuar\n")

                        #CONSULTAR
                        elif opcao_ec == 2:
                                os.system('cls')
                                print("\n==== SISTEMA DE CADASTRO DA FACOMP ====\n")

                                arquivo = open(arquivo_EC, 'r')

                                cadastro = []
                                cadastro = arquivo.readlines()

                                num = len(cadastro)
                                cont = 0
                                
                                while cont < num:
                                        print(" ===============\n Matricula:",cadastro[cont],"Nome:",cadastro[(cont+1)],"===============\n")
                                        cont = cont + 2

                                input("\nAperte ENTER para continuar")

                        #ALTERAR
                        elif opcao_ec == 3:
                                os.system('cls')
                                print("\n==== SISTEMA DE CADASTRO DA FACOMP====")

                                arquivo = open(arquivo_EC, 'r')
                                
                                cadastro = []
                                cadastro = arquivo.readlines()

                                cad = [s.strip() for s in cadastro] #remover os espaços em branco

                                num = len(cad)
                                cont = 0
                                busca = False

                                matricula = input("Digite a Matrícula: ")

                                while cont < num:
                                        if matricula == cad[cont]:
                                                cad[cont] = input("Nova Matrícula: ")
                                                cad[cont + 1] = input("Novo Nome: ")
                                                busca = True
                                                break

                                        cont = cont + 2
                                
                                if busca == False:
                                        print("\nMATRÍCULA NÃO ENCONTRADA!\n")
                                        input("\nAperte ENTER para continuar")

                                else:
                                        arquivo = open(arquivo_EC, 'w')

                                        cont = 0
                                        num = len(cad)

                                        while cont < num:
                                                arquivo.write(cad[cont])
                                                arquivo.write("\n")
                                                
                                                cont = cont + 1
                                        print("\nAlterado com sucesso!")
                                        input("\nAperte ENTER para continuar")

                        #EXCLUIR        
                        elif opcao_ec == 4:
                                os.system('cls')
                                print("\n==== SISTEMA DE CADASTRO DA FACOMP====")

                                arquivo = open(arquivo_EC, 'r')
                                
                                cadastro = []
                                cadastro = arquivo.readlines()

                                cad = [s.strip() for s in cadastro] #remover os espaços em branco

                                num = len(cad)
                                cont = 0
                                busca = False

                                matricula = input("Digite a Matrícula: ")

                                while cont < num:
                                        if matricula == cad[cont]:
                                                cad.pop(cont)
                                                cad.pop(cont)
                                                busca = True
                                                break

                                        cont = cont + 2
                                
                                if busca == False:
                                        print("\nMATRÍCULA NÃO ENCONTRADA!\n")
                                        input("\nAperte ENTER para continuar")

                                else:
                                        arquivo = open(arquivo_EC, 'w')

                                        cont = 0
                                        num = len(cad)

                                        while cont < num:
                                                arquivo.write(cad[cont])
                                                arquivo.write("\n")
                                                
                                                cont = cont + 1
                                        print("\nExcluído com sucesso!")
                                        input("\nAperte ENTER para continuar")
                        
                        #RETORNAR
                        elif opcao_ec == 5:
                                os.system('cls')
                                break

        #SISTEMAS
        elif opcao == 2:
                arquivo_SI = 'Provas/1ª avaliação/alunos_si.txt'
                escolha_si = 0

                while escolha_si != 5:
                        os.system('cls')
                        print("\n==== SISTEMA DE CADASTRO DA FACOMP ====")
                        print("Digite 1 para CADASTRAR")
                        print("Digite 2 para CONSULTAR")
                        print("Digite 3 para ALTERAR")
                        print("Digite 4 para EXCLUIR")
                        print("Digite 5 para RETORNAR")

                        opcao_si = int(input("\nDigite sua opção: "))

                        #CADASTRAR
                        if opcao_si == 1:
                                os.system('cls')
                                print("\n==== SISTEMA DE CADASTRO DA FACOMP ====")

                                arquivo = open(arquivo_SI, 'a')

                                arquivo.write(input("Insira a Matrícula: "))
                                arquivo.write("\n")
                                
                                arquivo.write(input("Insira o Nome: "))
                                arquivo.write("\n")

                                print("\nCadastrado com sucesso!")
                                input("\nAperte ENTER para continuar\n")

                        #CONSULTAR
                        elif opcao_si == 2:
                                os.system('cls')
                                print("\n==== SISTEMA DE CADASTRO DA FACOMP ====\n")

                                arquivo = open(arquivo_SI, 'r')

                                cadastro = []
                                cadastro = arquivo.readlines()

                                num = len(cadastro)
                                cont = 0
                                
                                while cont < num:
                                        print(" ===============\n Matricula:",cadastro[cont],"Nome:",cadastro[(cont+1)],"===============\n")
                                        cont = cont + 2

                                input("\nAperte ENTER para continuar")

                        #ALTERAR
                        elif opcao_si == 3:
                                os.system('cls')
                                print("\n==== SISTEMA DE CADASTRO DA FACOMP====")

                                arquivo = open(arquivo_SI, 'r')
                                
                                cadastro = []
                                cadastro = arquivo.readlines()

                                cad = [s.strip() for s in cadastro] #remover os espaços em branco

                                num = len(cad)
                                cont = 0
                                busca = False

                                matricula = input("Digite a Matrícula: ")

                                while cont < num:
                                        if matricula == cad[cont]:
                                                cad[cont] = input("Nova Matrícula: ")
                                                cad[cont + 1] = input("Novo Nome: ")
                                                busca = True
                                                break

                                        cont = cont + 2
                                
                                if busca == False:
                                        print("\nMATRÍCULA NÃO ENCONTRADA!\n")
                                        input("\nAperte ENTER para continuar")

                                else:
                                        arquivo = open(arquivo_SI, 'w')

                                        cont = 0
                                        num = len(cad)

                                        while cont < num:
                                                arquivo.write(cad[cont])
                                                arquivo.write("\n")
                                                
                                                cont = cont + 1
                                        print("\nAlterado com sucesso!")
                                        input("\nAperte ENTER para continuar")

                        #EXCLUIR        
                        elif opcao_si == 4:
                                os.system('cls')
                                print("\n==== SISTEMA DE CADASTRO DA FACOMP====")

                                arquivo = open(arquivo_SI, 'r')
                                
                                cadastro = []
                                cadastro = arquivo.readlines()

                                cad = [s.strip() for s in cadastro] #remover os espaços em branco

                                num = len(cad)
                                cont = 0
                                busca = False

                                matricula = input("Digite a Matrícula: ")

                                while cont < num:
                                        if matricula == cad[cont]:
                                                cad.pop(cont)
                                                cad.pop(cont)
                                                busca = True
                                                break

                                        cont = cont + 2
                                
                                if busca == False:
                                        print("\nMATRÍCULA NÃO ENCONTRADA!\n")
                                        input("\nAperte ENTER para continuar")

                                else:
                                        arquivo = open(arquivo_SI, 'w')

                                        cont = 0
                                        num = len(cad)

                                        while cont < num:
                                                arquivo.write(cad[cont])
                                                arquivo.write("\n")
                                                
                                                cont = cont + 1
                                        print("\nExcluído com sucesso!")
                                        input("\nAperte ENTER para continuar")
                        
                        #RETORNAR
                        elif opcao_si == 5:
                                os.system('cls')
                                break
        
        #SAIR
        elif opcao == 3:
                os.system('cls')
                print("\n==== SISTEMA DE CADASTRO DA FACOMP ====")
                print("\nPROGRAMA FECHADO!!\n")
                break
        
        #OPÇÃO INVÁLIDA
        else:
                os.system('cls')
                print("\n==== SISTEMA DE CADASTRO DA FACOMP ====")
                print("\nOpçao inválida!!")
                input("\nAperte ENTER para continuar\n")