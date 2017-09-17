title: SUPER DICAS! Exercício do Jogo da Velha 
slug: email-14-super-dicas-exercicio-jogo-da-velha
template: email

Eu disse que em uma semana eu te enviaria o meu algoritmo do jogo da velha. Certo?

Você já conseguiu fazer?

Eu fiquei me segurando pra não te mandar algumas dicas, mas não aguentei.

Ainda não vou te enviar o meu algoritmo hoje.
Mas vou te dar algumas **super dicas** para resolver esse exercício!
Então vamos lá ...

##Inicialização da matriz "tabuleiro"

Eu disse que precisaríamos criar uma matriz de 3X3. Lembra? Assunto da lição 9.

O fato é que o valor dessa matriz deveria ser inicializado, ou seja, armazenar os primeiros valores,
 com "_" para as linhas 1 e 2 e " " para a terceira linha.

Então, um bom inicio para esse algoritmo é assim:

```
algoritmo "JogoDaVelha"
var
  tabuleiro: vetor[1..3,1..3] de caractere
  i, j : inteiro
inicio
  
  //Inicialização do tabuleiro com "_" nas linhas 1 e 2 e " " na terceira linha
  //i é a linha e j é a coluna.
  para j de 1 ate 3 faca
       para i de 1 ate 2 faca
            tabuleiro[i,j] := "_"
       fimpara
       tabuleiro[3,j] := " "
  fimpara

  ....

```

##Impressão do tabuleiro

Agora que já temos o nosso tabuleiro inicializado com os valores "_" e " ",
a gente pode escrever o tabuleiro na tela. Veja abaixo uma forma de fazer isso.

```
    //Apresenta a situação atual do tabuleiro
    escreval("Neste momento o tabuleiro está assim:")
    escreval("   1   2   3")
    escreval("1 _", tabuleiro[1,1], "_|_", tabuleiro[1,2], "_|_", tabuleiro[1,3], "_")
    escreval("2 _", tabuleiro[2,1], "_|_", tabuleiro[2,2], "_|_", tabuleiro[2,3], "_")
    escreval("3  ", tabuleiro[3,1], " | ", tabuleiro[3,2], " | ", tabuleiro[3,3], " ")

```

Perceba como eu usei os espaços em cada linha que a gente escreve na tela.
O resultado desse trecho de código é esse:


```
   1   2   3
1 ___|___|___
2 ___|___|___
3    |   |      
```

Agora, suponhamos que nós atualizamos alguns valores da matriz tabuleiro como se fossem jogadas. Veja o exemplo abaixo.

```
tabuleiro[1,2] := "X"
tabuleiro[3,3] := "O"
```

Nesse caso o nosso tabuleiro seria impresso assim:

```
   1   2   3
1 ___|_X_|___
2 ___|___|___
3    |   | O    
```

##Atualização do tabuleiro

Agora pense o seguinte, como vou atualizar o tabuleiro com a jogada de cada jogador?
Simples, vamos assumir que o "jogador 1" é "X" e o "jogador 2" é "O".
Aí a gente pode verificar quem fez a jogada e escrever a letra certa...

Veja:


```
    se jogadorAtual = nomeJogador1 entao
       tabuleiro[linhaJogada,colunaJogada] := "X"
    senao
       tabuleiro[linhaJogada,colunaJogada] := "O"
    fimse
    
```

##Verificaçao do Ganhador

Essa talvez seja a parte mais difícil, do algoritmo.
Mas se usarmos o nosso raciocínio lógico, podemos descobrir se o jogo teve ou não o ganhador.

Pense comigo, tem 3 formas de ganhar o jogo da velha:

- **1ª forma de ganhar**: Se o jogador conseguir preencher uma coluna completa
- **2ª forma de ganhar**: Se o jogador conseguir preencher uma linha completa
- **3ª forma de ganhar**: Se o jogador conseguir preencher uma diagonal completa

Para fazer a verificação do ganhador do jogo, precisaremos utilizar os operadores lógicos E e OU
dentro de um SE-ENTÃO.

Vamos ver então como a gente pode verificar cada uma dessas formas de ganhar.

### Jogador preencheu uma coluna completa?

Para verificar se o jogador ganhou com a coluna, podemos fazer um LOOP com a variável "j"
e verificar se todos os valores das linhas da matriz são iguais a 'X' ou a 'O'.

Aí a gente pode usar o próprio valor que atendeu a verificação para identificar o ganhador do jogo.

Veja um exemplo.

```
    para j de 1 ate 3 faca
         //Verifica as colunas
         //_X_|_O_|_X_
         //_X_|_O_|_X_
         // X | O | X
         se ((tabuleiro[1,j] = "X") ou (tabuleiro[1,j] = "O")) e (tabuleiro[1,j] = tabuleiro[2,j]) e (tabuleiro[2,j] = tabuleiro[3,j]) entao
            vencedor := tabuleiro[1,j]
         fimse
    fimpara
    
```

### Jogador preencheu uma linha completa?

Para verificar se o jogador ganhou com a coluna, podemos seguir o mesmo raciocínio da coluna.

Veja: 

```
    para i de 1 ate 3 faca
         //Verifica as linhas
         //_X_|_X_|_X_
         //_O_|_O_|_O_
         // X | X | X
         se ((tabuleiro[i,1] = "X") ou (tabuleiro[i,1] = "O")) e (tabuleiro[i,1] = tabuleiro[i,2]) e (tabuleiro[i,2] = tabuleiro[i,3]) entao
            vencedor := tabuleiro[i,1]
         fimse
    fimpara
```

### Jogador preencheu uma diagonal completa?

Agora só precisamos verificar se uma das duas diagonais foram preenchidas pelo mesmo jogador.

Veja:

```
    //_X_|___|_X_
    //___|_X_|___
    // X |   | X
    se (((tabuleiro[2,2] = "X") ou (tabuleiro[2,2] = "O")) e ((tabuleiro[1,1] = tabuleiro[2,2]) e (tabuleiro[2,2] = tabuleiro[3,3])) ou ((tabuleiro[3,1] = tabuleiro[2,2]) e (tabuleiro[2,2] = tabuleiro[1,3]))) entao
       vencedor := tabuleiro[2,2]
    fimse
```

###O jogo deu Velha?

Por fim, também precisamos verificar se o jogo **deu velha**.
Para isso podemos verificar se todos os valores da matriz foram preenchidos.
Ou seja, verificamos se todos os valores são diferentes dos valores iniciais "_" e " ",
e se a variável "vencedor" que utilizamos ainda não foi preenchida.

```
    se ((vencedor <> "") e (tabuleiro[1,1] <> "_") e (tabuleiro[1,2] <> "_") e (tabuleiro[1,3] <> "_") e (tabuleiro[2,1] <> "_") e (tabuleiro[2,2] <> "_") e (tabuleiro[2,3] <> "_") e (tabuleiro[3,1] <> " ") e (tabuleiro[3,2] <> " ") e (tabuleiro[3,3] <> " ")) entao
         vencedor := "V"
    fimse
```

##Agora é a sua vez!

Com essas **super dicas** tenho certeza que a sua cabeça já está a mil
pensando em como continuar o algoritmo do jogo.

Perceba que já utilizamos a matriz da lição 9 e a estruturas de repetição PARA-FAÇA, SE-ENTÃO-SENÃO
e outros conceitos como variáveis, operadores lógicos (E e OU) etc.

Nada como a prática, pra gente aprender melhor as coisas né...?

Bom, Vou deixar você tentar terminar esse exercício sozinho.
Daqui a 4 dias eu te envio o meu algoritmo. Aí você me conta se conseguiu resolver ou não.

Bons estudos!