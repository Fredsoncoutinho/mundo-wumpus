# Importa a biblioteca random
import random
import os

# Define o tamanho da matriz
matrix_size = 0
    
# Inicializa a matriz como uma lista de listas vazias
Mundo = []

movimento_agente = []
voltou_mundo = []

def relatorio():
    global epocas, morte_poco, morte_wumpus, venceu, qtd_origem, voltou_mundo
    print()
    print("O jogo rodou "+ str(epocas)+ " vezes")
    print("Morte por poço: "+str(morte_poco))
    print("Morte por Wumpus: "+str(morte_wumpus))
    print("Achou ouro: "+ str(venceu))
    print("Voltou para origem: "+ str(qtd_origem))
    print(f"Matou o wumpus {matou} vezes")
    print()
    #print("Voltou nos mundos: ",str(voltou_mundo))
    #print("Movimentos: "+ str(movimento_agente))
        

def seedWorld(Mundo):
    global matriz_size
    # Define os símbolos a serem usados na matriz
    agente = 'A'
    wumpus = 'W'
    ouro = 'O'
    poco = 'P'
    vazio = 'V'
    
    
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            row.append(vazio)
        Mundo.append(row)
    
    # Coloca o agente na posição [0][0]
    Mundo[0][0] = agente
    
    # Gera uma lista de símbolos a serem colocados na matriz
    symbols = [wumpus, ouro]
    
    # Distribui proporcionalmente o número de buracos na matriz
    num_vazios = matrix_size * matrix_size - 1
    num_poco = max(2, round(num_vazios * 0.15))
    if matrix_size == 4:
        num_poco = 2
    symbols += ['P']*num_poco

       
    random.shuffle(symbols)
    #print(symbols)
    # Coloca os símbolos restantes na matriz
    for s in symbols:
        while True:
            i = random.randint(0, matrix_size-1)
            j = random.randint(0, matrix_size-1)
            posicao = [i,j]
            
            if Mundo[i][j] == vazio:
                Mundo[i][j] = s
                break
    
def verifica_valor(matrix, row, col, value):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        #print("Posição inválida!")
        return False

    if matrix[row][col].find(value) != -1:
        #print(f"O valor '{value}' está presente na posição ({row}, {col}) da matriz.")
        return True
    else:
        #print(f"O valor '{value}' não está presente na posição ({row}, {col}) da matriz.")
        return False
  

def moveElement(matrix, direction):
    global morte_wumpus, morte_poco, venceu, voltou_origem,qtd_origem, movimento_agente, possui_ouro,voltou_mundo, flecha, matou
    agentRow, agentCol = None, None,
    rows, cols = len(matrix), len(matrix[0])
    
    # Encontra a posição atual do agente
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j].find('A') != -1:
                agentRow, agentCol = i, j
                break
        if agentRow is not None:
            break

    
    # Calcula a nova posição do agente
    if direction == 'd':
        newRow, newCol = agentRow, agentCol + 1
    elif direction == 'e':
        newRow, newCol = agentRow, agentCol - 1
    elif direction == 'b':
        newRow, newCol = agentRow - 1, agentCol
    elif direction == 'c':
        newRow, newCol = agentRow + 1, agentCol
    else:
        #print("Movimento inválido!")
        return 
    # Verifica se a nova posição é válida
    x, y = newRow, newCol 
    if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
        percepcao = identificaPercepcao(matrix[newRow][newCol])
        posicao_atira = atiraFlecha(percepcao, newCol, newRow)
        if posicao_atira is not None:
            x, y = posicao_atira
            if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
                if flecha>0:
                    if "W" in matrix[x][y]:
                        matrix[x][y] = "M"
                        print("matou")
                        flecha = -1
                        print("numero de flechas ", flecha)
                        matou += 1
                    else:
                        print("não matou")
                        flecha = 0
                        print("numero de flechas ", flecha)
    
            
    
    if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols:
        #print('Movimento inválido!')
        #for i in reversed(range(matrix_size)):
        #    print(Mundo[i])
        return
    
    if newRow == 0 and newCol == 0 and possui_ouro == True:
        matrix[newRow][newCol] = "A"
        matrix[agentRow][agentCol] = 'V'
        voltou_origem = True
        qtd_origem += 1

        
        for i in reversed(range(matrix_size)):
            print(Mundo[i])
        #print("##############Voltou origem#############")
        #print()
        return False
    
    

    
    if "W" in matrix[newRow][newCol] or "P" in matrix[newRow][newCol]:
        if matrix[newRow][newCol] == "W":
            morte_wumpus += 1
            print("Morreu pelo Wumpus")
        else:
            morte_poco += 1
            print("Caiu no poço")
        matrix[newRow][newCol] = 'X'
        matrix[agentRow][agentCol] = 'V'
        movimento_agente.append([newRow,newCol])
        for i in reversed(range(matrix_size)):
            print(Mundo[i])
        
        #print('Morreu')
        return False 

    if matrix[newRow][newCol].find("O") == 0:
        #print("posição anterior: ",matrix[agentCol][agentRow])
        matrix[newRow][newCol] = matrix[newRow][newCol].replace('O', 'A')
        matrix[agentRow][agentCol] = matrix[agentRow][agentCol].replace('A', 'V')
  
        
        possui_ouro = True
        movimento_agente.append([newRow,newCol])
        for i in reversed(range(matrix_size)):
            print(Mundo[i])
        venceu += 1
        #print('Achou o Ouro')
        return 
     
    """
    # Verifica se a nova posição está vazia
    if matrix[newRow][newCol] != 'V':
        #print('Movimento inválido!')
        return
    """
    if matrix[newRow][newCol].find("V") != -1:
        # Move o agente para a nova posição preservando o valor "B" na célula atual
        matrix[newRow][newCol] = 'A' + matrix[newRow][newCol].replace('V', '')
        matrix[agentRow][agentCol] = matrix[agentRow][agentCol].replace('A', 'V')
        movimento_agente.append([newRow, newCol])
        
        for i in reversed(range(matrix_size)):
            print(Mundo[i])


    #print(newRow,newCol,possui_ouro)
    
    
def adicionarPercepcoes(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j].find("W") != -1:
                # Adiciona a percepção de fedor nas posições adjacentes
                if i > 0:
                    if matrix[i - 1][j] != 'W' and matrix[i - 1][j] != "P":
                        
                        matrix[i - 1][j] += 'F'
                if i < rows - 1:
                    if matrix[i + 1][j] != 'W' and matrix[i + 1][j] != "P":
                        matrix[i + 1][j] += 'F'
                if j > 0:
                    if matrix[i][j - 1] != 'W' and matrix[i][j - 1] != "P":
                        matrix[i][j - 1] += 'F'
                if j < cols - 1:
                    if matrix[i][j + 1] != 'W' and matrix[i][j + 1] != "P":
                        matrix[i][j + 1] += 'F'
            
            if matrix[i][j].find("P") != -1:
                # Adiciona a percepção de brisa nas posições adjacentes
                if i > 0:
                    if matrix[i - 1][j] != 'P' and matrix[i - 1][j] != "P":
                        matrix[i - 1][j] += 'B'
                if i < rows - 1:
                    if matrix[i + 1][j] != 'P' and matrix[i + 1][j] != "P":
                        matrix[i + 1][j] += 'B'
                if j > 0:
                    if matrix[i][j - 1] != 'P' and matrix[i][j - 1] != "P":
                        matrix[i][j - 1] += 'B'
                if j < cols - 1:
                    if matrix[i][j + 1] != 'P' and matrix[i][j + 1] != "P":
                        matrix[i][j + 1] += 'B'
            
            if matrix[i][j].find("O") != -1:
                # Adiciona a percepção de brilho na posição adjacente
                if i > 0:
                    if matrix[i - 1][j] != 'O' and matrix[i - 1][j] != "P":
                      
                        matrix[i - 1][j] += 'G'
                if i < rows - 1:
                    if matrix[i + 1][j] != 'O' and matrix[i + 1][j] != "P":
                        
                        matrix[i + 1][j] += 'G'
                if j > 0:
                    if matrix[i][j - 1] != 'O' and matrix[i][j - 1] != "P":
                        4
                        matrix[i][j - 1] += 'G'
                if j < cols - 1:
                    if matrix[i][j + 1] != 'O' and matrix[i][j + 1] != "P":
                        
                        matrix[i][j + 1] += 'G'


def identificaPercepcao(posicao):
    if "G" in posicao:
        print("percebeu brilho")
        return "G"
    if "F" in posicao:
        print("percebeu fedor")
        return "F"
    if "B" in posicao:
        print("percebeu brisa")
        return "B"
    print("Não identificou nada")
    return "N"


def atiraFlecha(percepcao, agentCol, agentRow):
    global flecha
    adjacents = []
    if percepcao == None:
        return 
    if "F" in percepcao:
        cima = [agentRow - 1, agentCol]
        baixo = [agentRow + 1, agentCol]
        direita = [agentRow, agentCol - 1]
        esquerda = [agentRow, agentCol + 1]
        
        adjacents += [cima]
        adjacents += [baixo]
        adjacents += [direita]
        adjacents += [esquerda]
        
        print(adjacents)
        
        posicao_atira = random.choice(adjacents)
        
        return posicao_atira
    
    
def iniciaMundo():
    global flecha, matrix_size, Mundo, epocas, possui_ouro, qtd_origem, voltou_mundo, voltou_origem, id_mundo
    """
    modo = input("deseja que seja manual ou automatico? [m/a] ")

    if modo == "m":
        lista_posicao = []
        resultado = input("digite a nova posição (c,b,d,e): ")
        matrix_size = int(input("Qual o tamanho do mundo? "))
        epocas = int(input("Quantas simulações dejesa fazer? "))
    else:
        matrix_size = int(input("Qual o tamanho do mundo? "))
        epocas = int(input("Quantas simulações dejesa fazer? "))
"""
    #adicionarPercepcoes(Mundo)  # Adiciona as per4
    matrix_size = int(input("Qual o tamanho do mundo? "))
    epocas = int(input("Quantas simulações dejesa fazer? "))
    for i in range(epocas):
        id_mundo = i
        if voltou_origem == True:
             voltou_mundo.append(id_mundo)
        possui_ouro = False
        flecha = 1
        Mundo= []
        seedWorld(Mundo)
        adicionarPercepcoes(Mundo)
        print()
        
        print("***************Mundo ",i,"***************")
        for i in reversed(range(matrix_size)):
                print(Mundo[i])
        while True:
            #os.system('clr||clear')
            # Imprime a matriz com as linhas invertidas
           
            #for i in reversed(range(matrix_size)):
                #if len(Mundo[i]) < 3:
                    #print(" "+Mundo[i]+" ")
                #else:
                 #print(Mundo[i])
            #print()
            
            lista_posicao = []
            #resultado = input("digite a nova posição (c,b,d,e): ")


            lista = ['c', 'b', 'e', 'd']
            resultado = random.choice(lista)
            

            #if possui_ouro:
                #print("Possui ouro!")

            print()
            for i in reversed(range(matrix_size)):
               print(Mundo[i])
            if moveElement(Mundo, resultado) == False:
                #print()
                break
            #print()
  
    relatorio()
    
    
   
    continua = input("Deseja continuar? [s/n] ")
    if continua == "n":
        exit()
    elif continua == "s":
        return
    else:
         print("Comando invalido")
         

while True:   
    id_mundo = None
    morte_poco = 0
    morte_wumpus = 0
    venceu = 0 
    qtd_origem =0
    possui_ouro = False 
    voltou_origem = False
    matou = 0
    flecha = 1
    iniciaMundo()
    