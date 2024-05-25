#OPÇÃO MANUAL E OPÇÃO AUTOMÁTICA
#3 PINOS
#N DISCOS

#GERAL
import os
os.system('cls')
#CRIAÇÃO DE LISTAS PARA CADA PINO DA TORRE
TorreA = []
TorreB = []
TorreC = []

#DEFINE TOTAL DE DISCOS E OS POSICIONA NA TORRE A
discos = int(input("Quantidade de discos: "))
for disco in range(discos, 0, -1):
    TorreA.append(disco)

print("Torre A: ", TorreA)
print("Torre B: ", TorreB)
print("Torre C: ", TorreC, "\n")

#GUARDA RESULTADO ESPERADO NO FINAL
objetivo = TorreA.copy()

#CRIAÇÃO DA FUNÇÃO DE RESOLUÇÃO MANUAL DO DESAFIO
def HanoiManual():
    #DECLARA CONTADOR DE JOGADAS
    mov = 0
    
    while TorreC != objetivo:
        #SELECIONA TORRE PARA COLOCAR O DISCO
        Remover = str(input("De qual torre remover disco: "))
        Inserir = str(input("Em qual torre colocar o disco?: "))

        os.system('cls')

        #SE TORRE ESCOLHIDA PRA REMOVER FOR A
        if Remover.upper() == "A":
            #SE TORRE A NÃO TIVER DISCO E TORRE PARA INSERIR EXISTIR
            if len(TorreA) == 0 and Inserir.upper() in ["A", "B", "C"]:
                print("Torre A vazia! Tente novamente. \n")

            #SE TORRE A NÃO TIVER DISCO E TORRE PARA INSERIR NÃO EXISTIR
            if len(TorreA) == 0 and Inserir.upper() not in ["A", "B", "C"]:
                print("Torre A vazia e movimento inválido! Tente novamente. \n")

            #SE TORRE A TIVER DISCO
            if len(TorreA) > 0:
                #SE TORRE ESCOLHIDA PRA INSERIR FOR A, FAZ USUÁRIO TENTAR NOVAMENTE
                if Inserir.upper() == "A":
                    print("Movimento inválido! Tente novamente. \n")

                #SE TORRE ESCOLHIDA PRA INSERIR FOR B
                if Inserir.upper() == "B":  
                    #SE DISCO NA TORRE B FOR MAIOR QUE O DA TORRE A OU SE TORRE ESTIVER VAZIA
                    if len(TorreB) == 0 or TorreB[-1] > TorreA[-1]:
                        #ADICIONA ÚLTIMO ITEM DA TORRE A NA TORRE B E REMOVE DA TORRE A
                        TorreB.append(TorreA[-1])
                        TorreA.pop()
                        mov += 1
                        print("Torre A: ", TorreA)
                        print("Torre B: ", TorreB)
                        print("Torre C: ", TorreC, "\n")
                    #SE DISCO NA TORRE B FOR MENOR QUE O DA TORRE A
                    else:
                        print("Movimento inválido! Tente novamente. \n")

                #SE TORRE ESCOLHIDA PRA INSERIR FOR C
                if Inserir.upper() == "C":
                    #SE DISCO NA TORRE C FOR MAIOR QUE O DA TORRE A OU SE TORRE ESTIVER VAZIA
                    if len(TorreC) == 0 or TorreC[-1] > TorreA[-1]:
                        #ADICIONA ÚLTIMO ITEM DA TORRE A NA TORRE C E REMOVE DA TORRE A
                        TorreC.append(TorreA[-1])
                        TorreA.pop()
                        mov += 1
                        print("Torre A: ", TorreA)
                        print("Torre B: ", TorreB)
                        print("Torre C: ", TorreC, "\n")
                    #SE DISCO NA TORRE C FOR MENOR QUE O DA TORRE A
                    else:
                        print("Movimento inválido! Tente novamente. \n")

                #SE TORRE ESCOLHIDA PRA INSERIR NÃO EXISTIR, FAZ USUÁRIO TENTAR NOVAMENTE
                if Inserir.upper() not in ["A", "B", "C"]:
                    print("Torre inexistente! Tente novamente. \n")

        #SE TORRE ESCOLHIDA PRA REMOVER FOR B
        if Remover.upper() == "B":
            #SE TORRE B NÃO TIVER DISCO E TORRE PARA INSERIR EXISTIR
            if len(TorreB) == 0 and Inserir.upper() in ["A", "B", "C"]:
                print("Torre B vazia! Tente novamente. \n")

            #SE TORRE B NÃO TIVER DISCO E TORRE PARA INSERIR NÃO EXISTIR
            if len(TorreB) == 0 and Inserir.upper() not in ["A", "B", "C"]:
                print("Torre B vazia e movimento inválido! Tente novamente. \n")

            #SE TORRE B TIVER DISCO
            if len(TorreB) > 0:
                #SE TORRE ESCOLHIDA PRA INSERIR FOR B, FAZ USUÁRIO TENTAR NOVAMENTE
                if Inserir.upper() == "B":
                    print("Movimento inválido! Tente novamente. \n")

                #SE TORRE ESCOLHIDA PRA INSERIR FOR A
                if Inserir.upper() == "A":  
                    #SE DISCO NA TORRE A FOR MAIOR QUE O DA TORRE B OU SE TORRE ESTIVER VAZIA
                    if len(TorreA) == 0 or TorreA[-1] > TorreB[-1]:
                        #ADICIONA ÚLTIMO ITEM DA TORRE B NA TORRE A E REMOVE DA TORRE B
                        TorreA.append(TorreB[-1])
                        TorreB.pop()
                        mov += 1
                        print("Torre A: ", TorreA)
                        print("Torre B: ", TorreB)
                        print("Torre C: ", TorreC, "\n")
                    #SE DISCO NA TORRE A FOR MENOR QUE O DA TORRE B
                    else:
                        print("Movimento inválido! Tente novamente. \n")

                #SE TORRE ESCOLHIDA PRA INSERIR FOR C
                if Inserir.upper() == "C":
                    #SE DISCO NA TORRE C FOR MAIOR QUE O DA TORRE B OU SE TORRE ESTIVER VAZIA
                    if len(TorreC) == 0 or TorreC[-1] > TorreB[-1]:
                        #ADICIONA ÚLTIMO ITEM DA TORRE B NA TORRE C E REMOVE DA TORRE B
                        TorreC.append(TorreB[-1])
                        TorreB.pop()
                        mov += 1
                        print("Torre A: ", TorreA)
                        print("Torre B: ", TorreB)
                        print("Torre C: ", TorreC, "\n")
                    #SE DISCO NA TORRE C FOR MENOR QUE O DA TORRE B
                    else:
                        print("Movimento inválido! Tente novamente. \n")

                #SE TORRE ESCOLHIDA PRA INSERIR NÃO EXISTIR, FAZ USUÁRIO TENTAR NOVAMENTE
                if Inserir.upper() not in ["A", "B", "C"]:
                    print("Torre inexistente! Tente novamente. \n")

        #SE TORRE ESCOLHIDA PRA REMOVER FOR C
        if Remover.upper() == "C":
            #SE TORRE C NÃO TIVER DISCO E TORRE PARA INSERIR EXISTIR
            if len(TorreC) == 0 and Inserir.upper() in ["A", "B", "C"]:
                print("Torre C vazia! Tente novamente. \n")

            #SE TORRE C NÃO TIVER DISCO E TORRE PARA INSERIR NÃO EXISTIR
            if len(TorreC) == 0 and Inserir.upper() not in ["A", "B", "C"]:
                print("Torre C vazia e movimento inválido! Tente novamente. \n")

            #SE TORRE C TIVER DISCO
            if len(TorreC) > 0:
                #SE TORRE ESCOLHIDA PRA INSERIR FOR C, FAZ USUÁRIO TENTAR NOVAMENTE
                if Inserir.upper() == "C":
                    print("Movimento inválido! Tente novamente. \n")

                #SE TORRE ESCOLHIDA PRA INSERIR FOR A
                if Inserir.upper() == "A":  
                    #SE DISCO NA TORRE A FOR MAIOR QUE O DA TORRE C OU SE TORRE ESTIVER VAZIA
                    if len(TorreA) == 0 or TorreA[-1] > TorreC[-1]:
                        #ADICIONA ÚLTIMO ITEM DA TORRE C NA TORRE A E REMOVE DA TORRE C
                        TorreA.append(TorreC[-1])
                        TorreC.pop()
                        mov += 1
                        print("Torre A: ", TorreA)
                        print("Torre B: ", TorreB)
                        print("Torre C: ", TorreC, "\n")
                    #SE DISCO NA TORRE A FOR MENOR QUE O DA TORRE C
                    else:
                        print("Movimento inválido! Tente novamente. \n")

                #SE TORRE ESCOLHIDA PRA INSERIR FOR B
                if Inserir.upper() == "B":
                    #SE DISCO NA TORRE B FOR MAIOR QUE O DA TORRE C OU SE TORRE ESTIVER VAZIA
                    if len(TorreB) == 0 or TorreB[-1] > TorreC[-1]:
                        #ADICIONA ÚLTIMO ITEM DA TORRE C NA TORRE B E REMOVE DA TORRE C
                        TorreB.append(TorreC[-1])
                        TorreC.pop()
                        mov += 1
                        print("Torre A: ", TorreA)
                        print("Torre B: ", TorreB)
                        print("Torre C: ", TorreC, "\n")
                    #SE DISCO NA TORRE B FOR MENOR QUE O DA TORRE C
                    else:
                        print("Movimento inválido! Tente novamente. \n")

                #SE TORRE ESCOLHIDA PRA INSERIR NÃO EXISTIR, FAZ USUÁRIO TENTAR NOVAMENTE
                if Inserir.upper() not in ["A", "B", "C"]:
                    print("Torre inexistente! Tente novamente. \n")    

    #QUANDO TORRE C ESTIVER COMPLETA, FINALIZA O JOGO
    print("DESAFIO CONCLUÍDO, PARABÉNS!")
    print("Você completou a Torre de Hanoi em", mov, "jogadas.")
    print("A Torre de Hanoi com", discos, "discos pode ser completada em", (2**discos) - 1, "jogadas.")

#FUNÇÃO DE RESOLUÇÃO AUTOMÁTICA
def HanoiAuto(numDiscos, inicio, fim, meio):
    #SE A QUANTIDADE DE DISCO NA TORRE A FOR 1
    if numDiscos == 1:
        #MOVE DISCO MENOR PARA TORRE C E REMOVE DA TORRE A
        disco = inicio.pop()
        fim.append(disco)
        print("Torre A: ", TorreA)
        print("Torre B: ", TorreB)
        print("Torre C: ", TorreC, "\n")
    #SE A QUANTIDADE DE DISCO NA TORRE A FOR DIFERENTE QUE 1
    else:
        HanoiAuto(numDiscos-1, inicio, meio, fim)
        disco = inicio.pop()
        fim.append(disco)
        print("Torre A: ", TorreA)
        print("Torre B: ", TorreB)
        print("Torre C: ", TorreC, "\n")
        HanoiAuto(numDiscos-1, meio, fim, inicio)


opcao = -1

while opcao != 0:
    opcao = int(input("[1] Resolução automática \n[2] Resolução manual \n[0] Sair \n: "))
    if opcao == 1:
        HanoiAuto(discos, TorreA, TorreC, TorreB)
        print("A TORRE DE HANOI FOI RESOLVIDA!")
        break
    elif opcao == 2:
        HanoiManual()
        break
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")


