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
    print(symbols)
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
        print("Posição inválida!")
        return False

    if matrix[row][col].find(value) != -1:
        print(f"O valor '{value}' está presente na posição ({row}, {col}) da matriz.")
        return True
    else:
        print(f"O valor '{value}' não está presente na posição ({row}, {col}) da matriz.")
        return False
  

def moveElement(matrix, direction):
    global morte_wumpus, morte_poco, venceu, voltou_origem,qtd_origem, movimento_agente, possui_ouro,voltou_mundo
    agentRow, agentCol = None, None
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
        print("Movimento inválido!")
        return 
    # Verifica se a nova posição é válida

    if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols:
        #print('Movimento inválido!')
        return
      
    if newRow == 0 and newCol == 0 and possui_ouro == True:
        matrix[newRow][newCol] = "A"
        matrix[agentRow][agentCol] = 'V'
        voltou_origem = True
        qtd_origem += 1
        print("Voltou origem ")
        
        for i in reversed(range(matrix_size)):
            print(Mundo[i])
        return False
    
    
    
    if matrix[newRow][newCol].find('W') != -1 or matrix[newRow][newCol].find('P') != -1:
        if matrix[newRow][newCol] == "W":
            morte_wumpus += 1
        else:
            morte_poco += 1
        matrix[newRow][newCol] = 'X'
        matrix[agentRow][agentCol] = 'V'
        movimento_agente.append([newRow,newCol])
        for i in reversed(range(matrix_size)):
            print(Mundo[i])
        
        
        print('Morreu')
        return False 
        
    if matrix[newRow][newCol] == 'O':
        if 'O' in matrix[newRow][newCol]:
            # Move o agente para a nova posição mantendo os caracteres existentes, exceto "O"
            matrix[newRow][newCol] = 'A' + matrix[newRow][newCol].replace('O', '')

        else:
            # Move o agente para a nova posição
            matrix[newRow][newCol] += 'A'
        #matrix[agentRow][agentCol] = 'V'
        possui_ouro = True
        movimento_agente.append([newRow,newCol])
        for i in reversed(range(matrix_size)):
            print(Mundo[i])
        venceu += 1
        print('Achou o Ouro')
        return 
     
    """
    # Verifica se a nova posição está vazia
    if matrix[newRow][newCol] != 'V':
        print('Movimento inválido!')
        return
    """
    if matrix[newRow][newCol].find("V") != -1:
        # Move o agente para a nova posição preservando o valor "B" na célula atual
        matrix[newRow][newCol] = 'A' + matrix[newRow][newCol].replace('V', '')
        matrix[agentRow][agentCol] = matrix[agentRow][agentCol].replace('A', 'V')
        movimento_agente.append([newRow, newCol])
    

    
    print(newRow,newCol,possui_ouro)
    
    
def adicionarPercepcoes(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'W':
                # Adiciona a percepção de fedor nas posições adjacentes
                if i > 0:
                    if matrix[i - 1][j] != 'W':
                        matrix[i - 1][j] += 'F'
                if i < rows - 1:
                    if matrix[i + 1][j] != 'W':
                        matrix[i + 1][j] += 'F'
                if j > 0:
                    if matrix[i][j - 1] != 'W':
                        matrix[i][j - 1] += 'F'
                if j < cols - 1:
                    if matrix[i][j + 1] != 'W':
                        matrix[i][j + 1] += 'F'
            
            if matrix[i][j] == 'P':
                # Adiciona a percepção de brisa nas posições adjacentes
                if i > 0:
                    if matrix[i - 1][j] != 'P':
                        matrix[i - 1][j] += 'B'
                if i < rows - 1:
                    if matrix[i + 1][j] != 'P':
                        matrix[i + 1][j] += 'B'
                if j > 0:
                    if matrix[i][j - 1] != 'P':
                        matrix[i][j - 1] += 'B'
                if j < cols - 1:
                    if matrix[i][j + 1] != 'P':
                        matrix[i][j + 1] += 'B'
            
            if matrix[i][j] == 'O':
                # Adiciona a percepção de brilho na posição adjacente
                if i > 0:
                    if matrix[i - 1][j] != 'O':
                        matrix[i - 1][j] += 'G'
                if i < rows - 1:
                    if matrix[i + 1][j] != 'O':
                        matrix[i + 1][j] += 'G'
                if j > 0:
                    if matrix[i][j - 1] != 'O':
                        matrix[i][j - 1] += 'G'
                if j < cols - 1:
                    if matrix[i][j + 1] != 'O':
                        matrix[i][j + 1] += 'G'


def iniciaMundo():
    global matrix_size, Mundo, epocas, possui_ouro, qtd_origem, voltou_mundo, voltou_origem, id_mundo

    matrix_size = int(input("Qual o tamanho do mundo? "))
    epocas = int(input("Quantas simulações dejesa fazer? "))
    #adicionarPercepcoes(Mundo)  # Adiciona as per4
    
    for i in range(epocas):
        id_mundo = i
        if voltou_origem == True:
             voltou_mundo.append(id_mundo)
        possui_ouro = False
        Mundo= []
        seedWorld(Mundo)
        adicionarPercepcoes(Mundo)
        print("Mundo ",i)
        while True:
            #os.system('clr||clear')
            # Imprime a matriz com as linhas invertidas
           
            for i in reversed(range(matrix_size)):
                #if len(Mundo[i]) < 3:
                    #print(" "+Mundo[i]+" ")
                #else:
                 print(Mundo[i])
            print()
            
            #lista_posicao = []
            #resultado = input("digite a nova posição (c,b,d,e): ")
            
            lista = ['c', 'b', 'e', 'd']
            resultado = random.choice(lista)
        
            if possui_ouro:
                print("Possui ouro!")
            
            if moveElement(Mundo, resultado) == False:
                print()
                break
            print()
  
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
    
    iniciaMundo()
    