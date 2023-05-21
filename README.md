## O mundo de wumpus
## Engenharia Elétrica
# Disciplina: Inteligência Computacional - CO18036 (2023.02 – T01)

**Docente**: Prof. Dr. Otavio Noura Teixeira

**Discente 1**: Fredson Coutinho de Araújo Junior-201933940014

**Discente 2**: Willian Rodrigues Xavier-201933940022

## INTRODUÇÃO
O jogo "Mundo de Wumpus" é uma simulação de aventura baseada em texto que desafia os jogadores a explorar um ambiente perigoso em busca de um tesouro valioso. O objetivo principal é encontrar o tesouro e retornar em segurança à posição inicial, evitando armadilhas mortais e criaturas hostis.

No jogo, o mundo é representado por uma matriz de células interconectadas. Cada célula pode conter diferentes elementos, como o jogador, o tesouro, poços e o temível Wumpus. O jogador controla um agente explorador e deve se movimentar estrategicamente pela matriz, buscando pistas e evitando ameaças.

Uma das características marcantes do "Mundo de Wumpus" é a presença do Wumpus, uma criatura feroz que pode ser encontrada em uma das células do mundo. O jogador deve evitar entrar na célula ocupada pelo Wumpus, pois isso resultará em uma derrota imediata. Além disso, existem poços espalhados pelo mundo, e se o jogador cair em um deles, também será derrotado. A presença de pistas como o cheiro de Wumpus e a brisa dos poços ajuda o jogador a evitar esses perigos.

A estratégia desempenha um papel crucial no jogo, uma vez que o jogador precisa tomar decisões cuidadosas sobre quais células explorar e como se movimentar. É importante avaliar as pistas disponíveis, como o cheiro e a brisa, para determinar a presença do Wumpus ou de poços nas células vizinhas. Além disso, é necessário mapear o mundo conforme o jogador se move, anotando as descobertas e evitando retornar a células já visitadas.

O jogo "Mundo de Wumpus" é um desafio intelectual, pois exige raciocínio lógico, tomada de decisões e habilidades estratégicas dos jogadores. É necessário balancear a exploração do ambiente com a necessidade de evitar ameaças em potencial. Além disso, o fator aleatório das pistas e da localização do tesouro torna cada partida única e imprevisível.

Ao final de cada jogo, o jogador recebe um relatório com informações estatísticas, como o número de tentativas, mortes por Wumpus ou poços, e se o tesouro foi encontrado e recuperado com sucesso. Esses dados incentivam o jogador a melhorar sua estratégia e tentar novamente, criando uma experiência desafiadora e envolvente.

Em resumo, o jogo "Mundo de Wumpus" proporciona aos jogadores uma aventura emocionante, onde eles precisam usar suas habilidades de raciocínio e estratégia para explorar um ambiente perigoso, encontrar o tesouro e sobreviver aos perigos que espreitam em cada canto. É uma experiência estimulante que testa a astúcia e a coragem dos jogadores, enquanto os transporta para um mundo repleto de mistérios e desafios emocionantes.O jogo "Mundo de Wumpus" é uma simulação de aventura baseada em texto que desafia os jogadores a explorar um ambiente perigoso em busca de um tesouro valioso. O objetivo principal é encontrar o tesouro e retornar em segurança à posição inicial, evitando armadilhas mortais e criaturas hostis.

No jogo, o mundo é representado por uma matriz de células interconectadas. Cada célula pode conter diferentes elementos, como o jogador, o tesouro, poços e o temível Wumpus. O jogador controla um agente explorador e deve se movimentar estrategicamente pela matriz, buscando pistas e evitando ameaças.

Uma das características marcantes do "Mundo de Wumpus" é a presença do Wumpus, uma criatura feroz que pode ser encontrada em uma das células do mundo. O jogador deve evitar entrar na célula ocupada pelo Wumpus, pois isso resultará em uma derrota imediata. Além disso, existem poços espalhados pelo mundo, e se o jogador cair em um deles, também será derrotado. A presença de pistas como o cheiro de Wumpus e a brisa dos poços ajuda o jogador a evitar esses perigos.

A estratégia desempenha um papel crucial no jogo, uma vez que o jogador precisa tomar decisões cuidadosas sobre quais células explorar e como se movimentar. É importante avaliar as pistas disponíveis, como o cheiro e a brisa, para determinar a presença do Wumpus ou de poços nas células vizinhas. Além disso, é necessário mapear o mundo conforme o jogador se move, anotando as descobertas e evitando retornar a células já visitadas.

O jogo "Mundo de Wumpus" é um desafio intelectual, pois exige raciocínio lógico, tomada de decisões e habilidades estratégicas dos jogadores. É necessário balancear a exploração do ambiente com a necessidade de evitar ameaças em potencial. Além disso, o fator aleatório das pistas e da localização do tesouro torna cada partida única e imprevisível.

Ao final de cada jogo, o jogador recebe um relatório com informações estatísticas, como o número de tentativas, mortes por Wumpus ou poços, e se o tesouro foi encontrado e recuperado com sucesso. Esses dados incentivam o jogador a melhorar sua estratégia e tentar novamente, criando uma experiência desafiadora e envolvente.

Em resumo, o jogo "Mundo de Wumpus" proporciona aos jogadores uma aventura emocionante, onde eles precisam usar suas habilidades de raciocínio e estratégia para explorar um ambiente perigoso, encontrar o tesouro e sobreviver aos perigos que espreitam em cada canto. É uma experiência estimulante que testa a astúcia e a coragem dos jogadores, enquanto os transporta para um mundo repleto de mistérios e desafios emocionantes.

## **[ETAPA 1]()** *(Concluída)*

O código fornecido é uma implementação de um jogo baseado em uma matriz, onde um agente precisa navegar por um mundo em busca de um tesouro, evitando poços e um monstro chamado Wumpus.
 Abaixo descreve de forma detalhada o desenvolvimento para concluir a etapa 1:
**1.** A biblioteca `random` será usada para gerar números aleatórios, enquanto a biblioteca `os` permitirá a interação com o sistema operacional.

**2.** Em seguida, são definidas algumas variáveis globais:
   - **matrix_size** é inicializada como 0 e representa o tamanho da matriz do mundo.
   - **Mundo** é uma lista de listas vazias que será usada para representar o mundo do jogo.
   - **movimento_agente** é uma lista vazia que armazenará os movimentos realizados pelo agente durante o jogo.
   - **voltou_mundo** é uma lista vazia que armazenará os identificadores dos mundos em que o agente retornou à origem.

**3.** A função `relatorio()` é definida. Essa função imprimirá um relatório com informações sobre o jogo, incluindo o número de vezes que o jogo foi executado (`epocas`), o número de mortes causadas por poços (`morte_poco`), o número de mortes causadas pelo Wumpus (`morte_wumpus`), o número de vezes que o agente encontrou o tesouro (`venceu`), o número de vezes que o agente voltou à origem (`qtd_origem`), e uma lista de identificadores dos mundos em que o agente voltou (`voltou_mundo`).

**4.** A função `seedWorld(Mundo)` é definida. Essa função recebe a matriz do mundo como parâmetro e a preenche com símbolos representando o agente, o Wumpus, o tesouro, poços e células vazias.
   - Primeiro, o tamanho da matriz é determinado pela variável `matrix_size`.
   - Em seguida, a matriz é inicializada como uma lista de listas vazias.
   - O agente é colocado na posição [0][0] da matriz, representando a posição inicial do jogo.
   - A função gera uma lista de símbolos contendo o Wumpus, o tesouro e "P" (representando poços).
   - O número de poços é calculado com base no tamanho da matriz. Ele é definido como no mínimo 2 e representa aproximadamente 15% das células vazias da matriz.
   - Os símbolos são embaralhados aleatoriamente para garantir uma distribuição aleatória no mundo.
   - Em seguida, os símbolos restantes (Wumpus, tesouro e poços) são colocados na matriz em posições aleatórias, desde que a célula esteja vazia.

**5.** A função `verifica_valor(matrix, row, col, value)` é definida. Essa função recebe a matriz, as coordenadas (linha e coluna) e um valor como parâmetros.
   - A função verifica se a posição indicada pelas coordenadas (linha e coluna) é válida dentro da matriz.
   - Se o valor especificado estiver presente na posição indicada, uma mensagem é exibida indicando que o valor está presente na célula.
   - Caso contrário, uma mensagem é exibida informando que o valor não está presente na célula.
   
**6.** A etapa `moveElement()` no código acima é responsável por realizar os movimentos do agente dentro do mundo do jogo. Essa função recebe como parâmetros a matriz que representa o mundo e a direção na qual o agente deve se mover.

Primeiro, a função localiza a posição atual do agente na matriz, percorrendo todas as células até encontrar aquela que contém o símbolo do agente ('A'). Uma vez encontrada a posição do agente, são calculadas as coordenadas da nova posição com base na direção fornecida. As direções são representadas pelas letras 'd' (direita), 'e' (esquerda), 'b' (baixo) e 'c' (cima).

Em seguida, a função verifica se a nova posição é válida. Caso a nova posição esteja fora dos limites da matriz, o movimento é considerado inválido e a função retorna sem efetuar a movimentação.

Caso a nova posição seja válida, são realizadas diferentes verificações para determinar as ações a serem tomadas pelo agente. Se a nova posição contiver o símbolo 'W', que representa o Wumpus, o agente é considerado morto por ter encontrado o monstro. O símbolo 'X' é então colocado na nova posição para marcar a morte do agente.

Se a nova posição contiver o símbolo 'P', representando um poço, o agente também é considerado morto e o símbolo 'X' é colocado na nova posição para indicar a morte.

Se a nova posição contiver o símbolo 'O', representando o tesouro, o agente encontra o tesouro com sucesso. Nesse caso, o símbolo 'A' é movido para a nova posição, mantendo todos os outros símbolos presentes na célula.

Por fim, se a nova posição estiver vazia ('V'), o agente realiza o movimento normalmente, atualizando o símbolo 'A' para a nova posição e removendo o símbolo 'A' da posição anterior.

Após cada movimento, a função exibe a matriz atualizada, mostrando a posição do agente e quaisquer alterações feitas na célula.

Essa etapa é fundamental para controlar os movimentos do agente e verificar possíveis colisões com o Wumpus, poços ou o encontro do tesouro.

**7.** A função `adicionarPercepcoes(Mundo)` no código acima é responsável por adicionar percepções ao mundo do jogo com base na presença de elementos específicos, como o Wumpus, poços e o tesouro. Essas percepções são adicionadas às células adjacentes aos elementos correspondentes na matriz.

A função percorre cada célula da matriz `Mundo` e verifica se ela contém algum elemento especial, como o Wumpus ('W'), poço ('P') ou tesouro ('O'). Se a célula contiver um desses elementos, a função adiciona a percepção correspondente nas células adjacentes.

Para o Wumpus, a percepção adicionada é o cheiro de fedor. A função verifica as células acima, abaixo, à esquerda e à direita da posição do Wumpus na matriz e, caso essas células não contenham outro Wumpus, adiciona o símbolo de fedor ('F') a elas.

Para os poços, a percepção adicionada é a brisa. A função verifica as células adjacentes aos poços na matriz e, caso essas células não contenham outro poço, adiciona o símbolo de brisa ('B') a elas.

Para o tesouro, a percepção adicionada é o brilho. A função verifica as células adjacentes ao tesouro na matriz e, caso essas células não contenham outro tesouro, adiciona o símbolo de brilho ('G') a elas.

Essas percepções adicionadas ao mundo do jogo são fundamentais para que o agente possa tomar decisões estratégicas com base nas informações disponíveis. Por exemplo, a presença de cheiro de fedor indica a proximidade do Wumpus, a brisa indica a presença de poços nas proximidades e o brilho indica a localização do tesouro.

Essa função contribui para a dinâmica do jogo, fornecendo pistas ao agente sobre o ambiente e auxiliando na sua tomada de decisões para evitar ameaças e alcançar o objetivo de encontrar o tesouro com segurança.

## **[ETAPA 2]()** *(Concluída)*

**1.**A função adicionarPercepcoes(matrix) é responsável por adicionar as percepções de "fedor", "brisa" e "brilho" nas posições adjacentes às células que contêm o Wumpus, o poço e o ouro, respectivamente.

Ela recebe como parâmetro uma matriz matrix, que representa o mundo do jogo, onde cada célula contém informações sobre os elementos presentes (agente, Wumpus, poço, ouro) e suas percepções.

A função percorre cada célula da matriz e verifica se contém o símbolo correspondente ao Wumpus, poço ou ouro. Caso encontre algum desses símbolos, ela adiciona a percepção correspondente (fedor, brisa ou brilho) nas posições adjacentes à célula.

Por exemplo, se a função encontra o símbolo "W" em uma célula, ela adiciona a percepção de fedor nas posições acima, abaixo, à esquerda e à direita dessa célula, desde que essas posições não contenham o símbolo "W" ou "P".

Essa função é importante para que o agente possa receber informações sobre as percepções do ambiente e tomar decisões com base nelas, como evitar movimentos que levem a células com fedor (indicando a presença do Wumpus) ou brisa (indicando a presença de um poço). Além disso, a percepção de brilho indica a presença do ouro, o objetivo principal do agente.

Essa função contribui para a lógica do jogo e para o comportamento do agente, permitindo que ele faça escolhas mais informadas durante sua exploração do ambiente.

**2.**A função identificaPercepcao(matrix, posicao) é responsável por identificar e retornar a percepção específica de uma determinada posição no ambiente do jogo.

Ela recebe dois parâmetros: a matriz matrix, que representa o mundo do jogo com suas células e informações, e a posicao, que indica a coordenada (linha, coluna) da célula da qual se deseja obter a percepção.

A função verifica o conteúdo da célula na posição especificada e identifica qual percepção está associada a esse conteúdo. Por exemplo, se a célula contém o símbolo "W", a função retorna a percepção de fedor, indicando a presença do Wumpus. Se a célula contém o símbolo "P", a função retorna a percepção de brisa, indicando a presença de um poço. E se a célula contém o símbolo "G", a função retorna a percepção de brilho, indicando a presença do ouro.

Essa função é importante para que o agente possa obter informações sobre as percepções de uma célula específica no ambiente. Com base nessa percepção, o agente pode tomar decisões e planejar seus próximos movimentos de forma mais inteligente. Por exemplo, se a percepção for de fedor, o agente pode evitar essa célula para evitar o confronto com o Wumpus. Se a percepção for de brisa, o agente pode evitar a célula para evitar cair em um poço. E se a percepção for de brilho, o agente sabe que encontrou o ouro e pode planejar sua rota para pegá-lo.

Em resumo, a função identificaPercepcao permite ao agente obter informações sobre as percepções do ambiente em uma posição específica, contribuindo para suas decisões e estratégias durante o jogo.

**3.**A função atiraFlecha(posicao, matrix) é responsável por simular o ato de o agente atirar uma flecha em uma determinada direção no ambiente do jogo.

Ela recebe dois parâmetros: posicao, que indica a posição atual do agente no jogo (coordenada linha e coluna), e matrix, que representa o ambiente do jogo com suas células e informações.

A função utiliza a posição atual do agente para determinar a direção em que a flecha será disparada. Por exemplo, se o agente estiver na posição (linha, coluna), a flecha será disparada na direção correspondente à linha acima (linha-1) ou abaixo (linha+1) e à mesma coluna.

Ao disparar a flecha, a função verifica se há algum Wumpus na direção em que a flecha foi disparada. Se houver um Wumpus na célula atingida pela flecha, o Wumpus é eliminado e a informação é atualizada na matriz matrix. Caso contrário, a flecha simplesmente passa pelo espaço vazio sem causar nenhum efeito.

Essa função é importante para que o agente possa se livrar dos Wumpus no ambiente. Ao atirar a flecha, o agente elimina qualquer Wumpus na direção em que a flecha foi disparada, tornando essa área segura para ser explorada.

Em resumo, a função atiraFlecha simula o ato de atirar uma flecha em uma determinada direção no ambiente do jogo, permitindo que o agente elimine Wumpus e torne o ambiente mais seguro para exploA função atiraFlecha(posicao, matrix) é responsável por simular o ato de o agente atirar uma flecha em uma determinada direção no ambiente do jogo.

Ela recebe dois parâmetros: posicao, que indica a posição atual do agente no jogo A função atiraFlecha(posicao, matrix) é responsável por simular o ato de o agente atirar uma flecha em uma determinada direção no ambiente do jogo.

Ela recebe dois parâmetros: posicao, que indica a posição atual do agente no jogo (coordenada linha e coluna), e matrix, que representa o ambiente do jogo com suas células e informações.

A função utiliza a posição atual do agente para determinar a direção em que a flecha será disparada. Por exemplo, se o agente estiver na posição (linha, coluna), a flecha será disparada na direção correspondente à linha acima (linha-1) ou abaixo (linha+1) e à mesma coluna.

Ao disparar a flecha, a função verifica se há algum Wumpus na direção em que a flecha foi disparada. Se houver um Wumpus na célula atingida pela flecha, o Wumpus é eliminado e a informação é atualizada na matriz matrix. Caso contrário, a flecha simplesmente passa pelo espaço vazio sem causar nenhum efeito.

Essa função é importante para que o agente possa se livrar dos Wumpus no ambiente. Ao atirar a flecha, o agente elimina qualquer Wumpus na direção em que a flecha foi disparada, tornando essa área segura para ser explorada.

Em resumo, a função atiraFlecha simula o ato de atirar uma flecha em uma determinada direção no ambiente do jogo, permitindo que o agente elimine Wumpus e torne o ambiente mais seguro para explorar.(coordenada linha e coluna), e matrix, que representa o ambiente do jogo com suas células e informações.

A função utiliza a posição atual do agente para determinar a direção em que a flecha será disparada. Por exemplo, se o agente estiver na posição (linha, coluna), a flecha será disparada na direção correspondente à linha acima (linha-1) ou abaixo (linha+1) e à mesma coluna.

Ao disparar a flecha, a função verifica se há algum Wumpus na direção em que a flecha foi disparada. Se houver um Wumpus na célula atingida pela flecha, o Wumpus é eliminado e a informação é atualizada na matriz matrix. Caso contrário, a flecha simplesmente passa pelo espaço vazio sem causar nenhum efeito.

Essa função é importante para que o agente possa se livrar dos Wumpus no ambiente. Ao atirar a flecha, o agente elimina qualquer Wumpus na direção em que a flecha foi disparada, tornando essa área segura para ser explorada.

Em resumo, a função atiraFlecha simula o ato de atirar uma flecha em uma determinada direção no ambiente do jogo, permitindo que o agente elimine Wumpus e torne o ambiente mais seguro para explorar.